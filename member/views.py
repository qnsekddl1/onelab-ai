import json
import secrets
import smtplib
import ssl
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from sys import platform

from rest_framework.templatetags.rest_framework import data

ssl._create_default_https_context = ssl._create_unverified_context

from allauth.socialaccount.models import SocialAccount
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, MemberFile
from member.serializers import MemberSerializer
from oneLabProject import settings
from university.models import University




class MemberCheckIdView(APIView):
    def get(self, request):
        member_id = request.GET['member-id']
        is_duplicated = Member.objects.filter(member_id=member_id).exists()
        return Response({'isDup': is_duplicated})


class MemberNormalJoinView(View):
    def get(self, request):
        context = {
            'memberEmail': request.GET.get('member_email'),
            'memberSchoolEmail': request.GET.get('member_school_email'),
            'id': request.GET.get('id')
        }

        return render(request, 'login/normal-student-join.html', context)

    @transaction.atomic
    def post(self, request):
        data = request.POST
        university_major = data['university-member-major']
        data = {
            'member_name': data['member-name'],
            'member_password': data['member-password'],
            'member_email': data['member-email'],
            'member_school_email': data['member-school-email'],
            'member_phone': data['member-phone'],

        }

        member = Member.objects.create(**data)

        # member = Member.objects.filter(id=request.POST.get('id'))
        # # OAuth 최초 로그인 후 회원가입 시
        # if member.exists():
        #     del data['member_email']
        #     data['updated_date'] = timezone.now()
        #     member.update(**data)
        #
        # else:
        #     member = Member.objects.create(**data)
        member = Member.objects.get(id=member.id)
        university_info = {
            'university_member_birth': "1999-09-22",
            'university_member_major': university_major,
            'member': member
        }
        print(university_info)

        University.objects.create(**university_info)

        return redirect('member:login')


class MemberJoinView(View):
    def get(self, request):
        print(request.GET.get('member_name'))
        context = {
            'memberEmail': request.GET.get('member_email'),
            'memberType': request.GET.get('member_type'),
            'memberName': request.GET.get('member_name'),
            'memberPhone': request.GET.get('member_phone'),
            'memberSchoolEmail': request.GET.get('member_school_email')
        }
        # member_info = request.session['join-member-data']
        # context = {
        #     'member_email': member_info['member_email'],
        #     'member_name': member_info['member_name']
        # }

        return render(request, 'login/college-student-join.html', context)

    @transaction.atomic
    def post(self, request):
        data = request.POST
        user = SocialAccount.objects.get(user=request.user)
        university_major = data['university-member-major']
        data = {
            # 'member_name': data['member-name'],
            'member_phone': data['member-phone'],
            # 'member_password': data['member-password'],
            # 'member_email': data['member-email'],
            'member_school_email': data['member-school-email'],
        }
        last_member = Member.objects.latest('id')

        # OAuth 검사
        # OAuth 최초 로그인 시 TBL_MEMBER에 INSERT된 회원 ID가 member_id 이다.
        member = Member.objects.filter(id=last_member.id, member_type='naver')
        #   1. 아이디는 중복이 없다
        #   2. 이메일과 타입에 중복이 있다.
        #   3. OAuth로 최초 로그인된 회원을 찾아라

        # OAuth 최초 로그인 후 회원 가입
        if member.exists():
            print("존재함")
            # del data['member_email']
            # data['updated_date'] = timezone.now()
            member.update(**data)

        else:
            print("존재함1")
            member = Member.objects.create(**data)

        member = Member.objects.get(id=last_member.id)
        university_info = {
            'university_member_birth': "1999-09-22",
            'university_member_major': university_major,
            'member': member
        }
        print(university_info, member.__dict__)

        University.objects.create(**university_info)

        return redirect('member:login')


class MemberLoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        data = request.POST
        data = {
            'member_email': data['member-email'],
            'member_password': data['member-password']
        }

        member = Member.objects.filter(member_email=data['member_email'], member_password=data['member_password'])
        # print(member)
        url = '/'
        if member.exists():
            # 성공
            request.session['member'] = MemberSerializer(member.first()).data
            url = '/'
            return redirect('/')

        return render(request, 'login/login.html', {'check': False})


class SendVerificationCodeView(APIView):
    def post(self, request, school):
        data = request.POST
        # data = {
        #     # 'member_email': data['member-email'],
        #     'member_school_email': data['member-school-email'],
        # }
        # print(data['member-school-email'])
        # mail_receiver = data.get('member_school_email')
        # mail_receiver = json.dump(data)
        mail_receiver = school
        print(mail_receiver)
        rn = ''.join(random.choices('0123456789', k=6))


        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "wmoon0024@gmail.com"
        receiver_email = mail_receiver
        password = "pqxh ciic adcg numz"
        message = f"<h1>인증번호 6자리 입니다 : {rn}</h1>"

        print("메일 들어옴")
        msg = MIMEText(message, 'html')
        data = MIMEMultipart()
        data.attach(msg)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            print("들어옴1")
            server.starttls(context=context)
            print("들어옴2")
            server.ehlo()
            print("들어옴3")
            server.login(sender_email, password)
            print("들어옴4")
            server.sendmail(sender_email, receiver_email, data.as_string())
            # print("들어옴5")
            # server.quit()
        # server.sendmail(sender_email, receiver_email, data.as_string())
        # uri = request.get_full_path()
        # request.session['previous_uri'] = uri
        # previous_page = request.META.get('HTTP_REFERER')
        # return render(previous_page)
        # return JsonResponse({'success': True, 'message': '성공!!!'})

class MemberIdSearchView(View):
    def get(self, request):
        return render(request, 'login/account-find.html')

class MemberActivateEmailView(APIView):
    def get(self,request):
        pass

    def post(self, request, email):
        # data = request.POST
        # data = {
        #     'member_email': data['member_email']
        # }

        members = Member.objects.all()
        member_email = Member.objects.get(member_email=email)
        member_id = member_email.id
        print(member_id)
        print("id 들어옴")
        # print(member_id)


        # 랜덤 숫자랑 문자열 10자리
        # 이메일 링크를 받으면 적어도 그 링크를 통해 접속이 된다.
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # 세션에 랜덤 코드 추가
        request.session['random_code'] = code
        # # 세션 저장
        # request.session.save()

        print(request.session['random_code'])

        # if member_email.exists():

        print(email)
        print(request.POST)
        # print(data['member-school-email'])
        mail_receiver = email
        # mail_receiver = json.dump(data)
        # mail_receiver = 'wmoon0024@gmail.com'
        print(mail_receiver)

        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = "wmoon0024@gmail.com"
        receiver_email = mail_receiver
        password = "pqxh ciic adcg numz"
        message = (f"<h1>비밀번호 계정 링크 입니다.</h1>\n"
                   f"<h2>http://127.0.0.1:10000/member/account-reset/{member_id}/{code}</h2>")

        print("메일 들어옴")
        msg = MIMEText(message, 'html')
        data = MIMEMultipart()
        data.attach(msg)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            print("들어옴1")
            server.starttls(context=context)
            print("들어옴2")
            server.ehlo()
            print("들어옴3")
            server.login(sender_email, password)
            print("들어옴4")
            server.sendmail(sender_email, receiver_email, data.as_string())

            return Response('fasjfksa')


class MemberResetPasswordView(View):
    def get(self, request, id, random):
        del request.session['random_code']
        print("아이디", id)
        print("랜덤", random)


        member = Member.objects.get(id=id)
        print("아이디13들어옴")
        print(member.id)

        data = {
            'id': member.id,
            'random': random
        }
        print("여기까지 들어옴")

        # if member.id == id:
        #     member.save(update_fields=['member_password'])
        # 수정된 정보가 있을 수 있기 때문에 세션 정보 최신화
        # request.session['member'] = MemberSerializer(Member.objects.get(id=request.session['member']['id'])).data
        # check = request.GET.get('check')
        # context = {'check': check}
        return render(request, 'login/reset-link.html', data)

    def post(self, request, id, random):
        print("패스워드쪽 들어옴")
        data = request.POST
        data = {

            'member_id': data['member-id'],
            'member_password': data['member-password'],
        }
        print("패스워드 들어옴1")

        member = Member.objects.get(id=id)
        member.member_password = data['member_password']
        print("패스워드 들어옴2")

        member.save(update_fields=['member_password'])
        print("패스워드 들어옴3")
        return render(request, 'login/login.html')


class MemberMainView(View):
    def get(self, request):
        # member_name = request.session.get('member_name')
        request.session['member_name'] = MemberSerializer(Member.objects.get(id=request.session['member']['id'])).data
        print(request.session['member_name'])
        member = request.session['member']['id']
        profile = MemberFile.objects.filter(member_id=member).first()

        default_profile_url = 'https://static.wadiz.kr/assets/icon/profile-icon-1.png'

        if profile is None :
            profile = default_profile_url
            context = {
                'profile' : profile
            }
            return render(request, 'main/main-page.html', context)
        else :
            context = {
                'profile': profile
            }

            return render(request, 'main/main-page.html',context)