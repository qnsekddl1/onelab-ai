from django.shortcuts import render
from django.views import View


class CommunityWriteView(View):
    def get(self, request):
        return render(request, 'community/community-write.html')

class CommunityListView(View):
    def get(self, request):
        return render(request, 'community/community-list.html')

class CommunityDetailView(View):
    def get(self, request):
        return render(request, 'community/community-detail.html')