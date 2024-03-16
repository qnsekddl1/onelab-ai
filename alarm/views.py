import math

from django.db import transaction
from django.db.models import F, Q
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from alarm.models import Alarm
from member.models import Member


# 마이페이지 알람 클릭했을 떄 데이터를 가져오는 view (마이페이지에서 클릭했을 때 페이지가 이동 됌)
class AlarmDetailView(View):
    def get(self, request):
        data = request.GET
        return render(request, 'alarm/alarm.html', data)


class AlarmPagiNationAPIView(APIView):
    def get(self, request, page):
        # 세션에 아이디가 있을때
        # member_id = request.session['member'].get('id')
        # 작성한 사람 member_id ==> 작성한 사람과 보낸 사람이 똑같음
        member_id = 1
        # 받은 사람 receiver_id 과 보낸사람은 session의 변수값을 넣어줘야함
        receiver_name = Member.objects.get(member_name='또치').member_name
        # 보낸 사람 sender_id
        sender_name = Member.objects.get(member_name='또치').member_name

        row_count = 5
        offset = (page - 1) * row_count
        limit = page * row_count

        alarm_total_count = Alarm.objects.filter(((Q(alarm_receiver=receiver_name)|Q(alarm_sender=sender_name)) & ~Q(alarm_status=-1))).count()
        page_count = 5
        end_page =math.ceil(page / page_count) * page_count
        start_page = end_page - page_count + 1
        real_end = math.ceil(alarm_total_count / row_count)
        end_page = real_end if end_page > real_end else end_page

        # 보낸사람이 나이거나 작성한 사람이 나일때 보여줘야함

        alarm_objects = Alarm.objects.filter(((Q(alarm_receiver=receiver_name)|Q(alarm_sender=sender_name)) & ~Q(alarm_status=-1))).\
                            values\
                            ('id', 'alarm_receiver','alarm_sender','alarm_message', 'alarm_status','created_date','member__member_name', 'member_id','onelab__university_id' ).\
                            order_by('-created_date')[offset:limit]


        alarm_list = [{
            'id': alarm.get('id'),
            'alarm_receiver': alarm.get('alarm_receiver'),
            'alarm_sender': alarm.get('alarm_sender'),
            'alarm_message': alarm.get('alarm_message'),
            'alarm_status': alarm.get('alarm_status'),
            'created_date': alarm.get('created_date').strftime('%y-%m-%d'),
            'member_id': alarm.get('member_id'),
            'onelab_owner': alarm.get('onelab__university_id'),
            'member_name': alarm.get('member__member_name')
            # 'onelab_titie': alarm.get('onelab__onelab_main_title')
        } for alarm in alarm_objects]

        context = {
            'alarm_list': alarm_list,
            'alarm_total_count': alarm_total_count,
            'start_page': start_page,
            'end_page':end_page,
            'page': page,
            'real_end': real_end,
            'page_count': page_count
        }
        return Response(context)

class AlarmAgreeAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        alarm_id = data['alarmClickId']
        click_value = data['buttonResult']

        # 가입 승인
        Alarm.objects.filter(id=alarm_id, alarm_status=2).update(alarm_status = 0,alarm_message = click_value)

        return Response("success")

class AlarmDenyAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        alarm_id = data['alarmClickId']
        click_value = data['buttonResult']

        # 가입 거절
        Alarm.objects.filter(id=alarm_id, alarm_status=2).update(alarm_status=1, alarm_message=click_value)

        return Response("success")





