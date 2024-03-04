from django.urls import path

from community.views import CommunityWriteView, CommunityListView, CommunityDetailView

app_name = 'community'

urlpatterns = [
    path('write/', CommunityWriteView.as_view(), name='community-write'),
    path('list/', CommunityListView.as_view(), name='community-list'),
    path('detail/', CommunityDetailView.as_view(), name='community-detail')
]