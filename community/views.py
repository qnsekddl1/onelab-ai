from django.shortcuts import render, redirect
from django.views import View

from community.models import Community, CommunityFile
from member.models import Member


class CommunityWriteView(View):
    def get(self, request):
        return render(request, 'community/community-write.html')

    def post(self, request):
        data = request.POST

        files =request.FILES.getlist('upload-file')

        member = Member(**request.session['member'])

        data = {
            'community_title': data['community_title'],
            'community_content': data['community_content'],
            'community_status': data['community_status'],
            'member': member
        }
        community = Community.objects.create(**data)

        for file in files:
            CommunityFile.objects.create(community=community, path=file)

        return redirect(community.get_absolute_url())

class CommunityListView(View):
    def get(self, request):
        return render(request, 'community/community-list.html')

class CommunityDetailView(View):
    def get(self, request):
        return render(request, 'community/community-detail.html')