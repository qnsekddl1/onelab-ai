from profile import Profile

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone

from community.models import Community, CommunityFile
from highschool.models import HighSchool
from member.models import Member, MemberFile
from member.serializers import MemberSerializer
from point.serializers import PointSerializer
from point.models import Point
from school.models import School
from share.models import Share, SharePoints
from university.models import University
from file.models import File
from django.core.exceptions import ObjectDoesNotExist
import math
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math


class MyPageMainView(View):
    def get(self, request):
        member_id = request.session['member']['id']
        members = Member(**request.session['member'])
        university = University.objects.filter(member_id=member_id)
        highschool = HighSchool.objects.filter(member_id=member_id)
        school = School.objects.filter(member_id=member_id)
        profile = MemberFile.objects.filter(member_id=member_id).first()

        point = request.GET.get('point')
        # 커뮤니티 목록 가져오기
        community = Community.objects.filter(member_id=member_id, community_status=0).order_by('-id')

        # 세션 정보 최신화
        request.session['member'] = MemberSerializer(Member.objects.get(id=request.session['member']['id'])).data
        check = request.GET.get('check')

        # 페이징 처리
        page = request.GET.get('page', 1)
        row_count = 5
        paginator = Paginator(community, row_count)

        try:
            communities = paginator.page(page)
        except PageNotAnInteger:
            communities = paginator.page(1)
        except EmptyPage:
            communities = paginator.page(paginator.num_pages)

        # 페이지 관련 변수 계산
        # page_count = 5
        # end_page = math.ceil(page / page_count) * page_count
        # start_page = end_page - page_count + 1
        # real_end = math.ceil(paginator.count / row_count)
        # end_page = real_end if end_page > real_end else end_page

        # if end_page == 0:
        #     end_page = 1

        default_profile_url = 'https://static.wadiz.kr/assets/icon/profile-icon-1.png'

        if profile is None:
            profile = default_profile_url

        context = {
            'members': request.session['member'],
            'member_id': member_id,
            # 'highschool': highschool,
            'profile': profile,
            'check': check,
            'communities': communities,
        }

        if highschool:
            context['community_file'] = CommunityFile.objects.filter(community_id=community.first()).first()
            context['highschool'] = highschool
            print(community)

        if university:
            context['community_file'] = CommunityFile.objects.filter(community_id=community.first()).first()
            context['current_point'] = university.first().university_member_points
            context['university'] = University.objects.get(member_id=member_id)
        return render(request,'mypage/main-high.html' if highschool else 'mypage/main-university.html' if university else 'mypage/main.html',context)

    def post(self, request):
        data = request.POST
        file = request.FILES.get('profile')  # 'profile'은 input의 name 속성

        print('POST 들어옴')
        member = Member.objects.get(id=request.session['member']['id'])
        member_file = MemberFile.objects.filter(member=member).first()
        print(member.id)

        if file:  # 파일이 존재하는 경우에만 처리
            if member_file is None:
                file_instance = File.objects.create(file_size=file.size)
                member_file = MemberFile.objects.create(member=member, file=file_instance, path=file)
            else:
                file_instance = member_file.file
                file_instance.file_size = file.size
                file_instance.save()
                member_file.path = file

            member_file.save()

        # member_files = list(member.memberfile_set.values('path'))
        request.session['member_files'] = list(member.memberfile_set.values('path'))
        print(request.session['member_files'])
        print(request.session['member_files'],'이것좀 봐바!!!!!')

        # if len(member_files) != 0:
        #     request.session['member_files'] = member_files
        return redirect('myPage:main')

class MyPageCommunityView(View):
    def get(self, request):
        member = Member.objects.get(id=request.session['member']['id'])
        community = Community.objects.get(member_id=member).first()
        community_file = CommunityFile.objects.filter(community_id=community).order_by('-id')
        context = {
            'community': community,
            'community_file': list(community.communityfile_set.all())
        }
        print(context.get('community_file'))
        return render(request,'mypage/main-high.html',context)


class DeleteProfileView(View):
    def post(self, request):
        new_profile_path = 'member/2024/03/10/default.jpg'
        member = request.session['member']['id']

        print('삭제기능 들어옴')
        request.session['member_files'] = new_profile_path

        try:
            profile = MemberFile.objects.get(member_id=member)
            print(profile)

            profile = MemberFile.objects.filter(member_id=member).update(path=new_profile_path)
            profile.save()
            print('프로필 업데이트 성공')
        except MemberFile.DoesNotExist:
            print('프로필이 존재하지 않습니다.')

        return JsonResponse({'message': '프로필 이미지가 업데이트되었습니다.'})

class MyPagePointView(View):
    def get(self, request):
        member = request.session['member']['id']

        try:
            # 충전한 포인트 내역 최신순
            charge_date = Point.objects.filter(member_id=member, point_status=2).order_by('-id')

            # 사용한 포인트 내역 최신순 --> 사용한 내역이 있어야 하므로 GET.get('내용',0)을 쓰자
            use_date = Point.objects.filter(member_id=member, point_status=1).order_by('-id')
            date = use_date.first()
            dates = charge_date.first()

            # 세션에 등록된 멤버가 대학생인 경우 get_point를 가져옴
            get_point = University.objects.get(member_id=member)


            # Point에서 아까 선언한 대학생 정보를 가져오고 사용한 포인트니까 point_status가 1번인걸 가져온다.
            use_id = Point.objects.filter(member_id=member, point_status=1).aggregate(Sum('point'))['point__sum']

            if use_id:
                use_point = use_id
            else:
                use_point = 0

            current_point = get_point.university_member_points  # 현재 남은 잔액

            time = dates.updated_date if dates else '사용내역 없음'
            use_time = date.updated_date if date else "없음"

            context = {
                'current_point': current_point,
                'use_point': use_point,
                'point': Point.objects.filter(member_id=member,point_status=2).aggregate(Sum('point'))['point__sum'],
                'time': time,
                'use_time': use_time
            }

            return render(request, 'mypage/point.html', context)
        except ObjectDoesNotExist: # ERROR 발생의 경우
            return render(request,'mypage/main-high.html')

    def post(self,request):
        member_id = request.session['member']['id']
        point = Point.objects.filter(member_id=member_id)
        request.session['point'] = PointSerializer(point.first()).data
        return redirect(request,'mypage:my_point')



        # member_id = request.session['member']['id']
        # university = University.objects.filter(member_id=member_id)
        # highschool = HighSchool.objects.filter(member_id=member_id)
        #
        # # 페이지 번호 가져오기
        # page = request.GET.get('page',1)
        #
        # # 작성 리스트 가져온다.
        # write_list = Community.objects.filter(member_id=member_id, community_status=0).order_by('-id')[:]
        # # write_files = CommunityFile.objects.filter(community_id=write_list).order_by('-id')
        #
        # # Paginator를 사용하여 페이지당 원하는 개수로 나누기
        # paginator = Paginator(write_list,8) # 8개씩 보여주기로 설정 (원하는 개수로 변경 가능)
        #
        # try:
        #     communities = paginator.page(page)
        # except EmptyPage:
        #     communities = paginator.page(paginator.num_pages)

        # context = {
        #     'members' : request.session['member'],
        #     'member_id' : member_id,
        #     'communities' : communities
        # }
        # if university :
        #     return render(request,'mypage/main-university.html',context)
        # elif highschool :
        #     return render(request,'mypage/main-high.html',context)
        # else :
        #     return render(request,'mypage/main.html',context)

class MemberLogoutView(View):
    def get(self, request):
        request.session.clear()
        return redirect('member:login')
