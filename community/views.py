import math
from django.db import transaction

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from community.models import Community, CommunityFile
from member.models import Member


class CommunityWriteView(View):
    def get(self, request):
        Member(**request.session['member'])
        return render(request, 'community/community-write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        files = request.FILES

        # member = Member.objects.get(id=request.session['member']['id']) #이거 주석 해제 하면 밑에 member 주석 해야함
        member = Member(**request.session['member'])

        data = {
            'member': member,
            # 'member': Member.objects.get(id=request.session['member']['id']),
            'community_title': data['community-title'],
            'community_content': data['community-content']
        }

        community = Community.objects.create(**data)

        for key in files:
            members = CommunityFile.objects.create(community=community, path=files[key])
        return redirect(community.get_absolute_url())



class CommunityDetailView(View):
    def get(self, request):
        community = Community.objects.get(id=request.GET['id'])

        community.update_date = timezone.now()
        community.save(update_fields=['updated_date'])

        context = {
            'community': community,
            'community_file': community.communityfile_set
        }
        return render(request, 'community/community-detail.html', context)

class CommunityListView(View):

    def get(self, request):
        context = {
            'communities': list(Community.enabled_objects.all()),
        }

        return render(request, 'community/community-list.html', context)

class CommunityDeleteView(View):
    def get(self, request):
        community = Community.objects.get(id=request.GET['id'])
        community.status = False
        community.updated_date = timezone.now()
        community.save(update_fields=['status', 'updated_date'])

        return redirect('community:list')

class CommunityUpdateView(View):
    def get(self, request):
        community = Community.objects.get(id=request.GET['id'])
        context = {
            'community': community,
            # 'community_file': list(community.communityfile_set.values('path'))
        }
        return render(request, 'community/community-update.html', context)

    @transaction.atomic
    def post(self, request):
        id = request.GET['id']
        datas = request.POST
        # files = request.FILES

        datas = {
            'community_title': datas['community-title'],
            'community_content': datas['community-content'],
            'member': Member.objects.get(id=request.session['member']['id'])
        }

        community = Community.objects.get(id=id)
        community.community_title = datas['community_title']
        community.community_content = datas['community_content']
        community.updated_date = timezone.now()
        community.save(update_fields=['community_title', 'community_content', 'updated_date'])

        # for key in files:
        #     CommunityFile.objects.create(community=community, path=files[key], preview=kye == 'upload1')

        return redirect(community.get_absolute_url())