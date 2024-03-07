# from django.shortcuts import render, redirect
# from django.views import View
#
# from community.models import Community, CommunityFile
# from member.models import Member
#
#
# class CommunityWriteView(View):
#     def get(self, request):
#         return render(request, 'community/community-write.html')
#
#     def post(self, request):
#         data = request.POST
#
#         files =request.FILES.getlist('upload-file')
#
#         member = Member(**request.session['member'])
#
#         data = {
#             'community_title': data['community_title'],
#             'community_content': data['community_content'],
#             'community_status': data['community_status'],
#             'member': member
#         }
#         community = Community.objects.create(**data)
#
#         for file in files:
#             CommunityFile.objects.create(community=community, path=file)
#
#         return redirect(community.get_absolute_url())
#
# class CommunityListView(View):
#     def get(self, request):
#         return render(request, 'community/community-list.html')
#
# class CommunityDetailView(View):
#     def get(self, request):
#         return render(request, 'community/community-detail.html')



import math

from django.db import transaction
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from community.models import Community
from member.models import Member


class CommunityWriteView(View):
    def get(self, request):
        return render(request, 'community/community-write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        files = request.FILES

        member = Member(**request.session['member'])

        data = {
            'member': member,
            'community_title': data['community-title'],
            'community_content': data['community-content']
        }

        community = Community.objects.create(**data)

        return redirect(community.get_absolute_url())

class CommunityDetailView(View):
    def get(self, request):
        community = Community.objects.get(id=request.GET['id'])
        community.updated_date = timezone.now()
        community.save(update_fields=['updated_date'])

        context = {
            'community': community,
            # 'community_files': list(community.community_files_set.all())
        }
        return render(request, 'community/community-detail.html', {'community': community})

class CommunityListView(View):
    def get(self, request):
        page = request.GET.get('page', 1)

        row_count = 5
        offset = (page - 1) * row_count
        limit = page * row_count
        total = Community.objects.all().count()
        page_count = 5
        end_page = math.ceil(page / page_count) * page_count
        start_page = end_page - page_count + 1
        real_end = math.ceil(total / row_count)
        end_page = real_end if end_page > real_end else end_page

        if end_page == 0:
            end_page = 1

        context = {
            'communities': list(Community.enabled_objects.all()[offset:limit]),
            'start_page': start_page,
            'end_page': end_page,
            'page': page,
            'real_end': real_end,
            'page_count': page_count,
        }

        return  render(request, 'community/community-list.html', context)

class CommunityDeleteView(View):
    def get(self, request):
        community = Community.objects.get(id=request.GET['id'])
        community.community_post_status = False
        community.updated_date = timezone.now()
        community.save(update_fields=['community_post_status', 'updated_date'])

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