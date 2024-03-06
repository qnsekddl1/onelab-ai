# from django.urls import path
#
# from community.views import CommunityWriteView, CommunityListView, CommunityDetailView
#
# app_name = 'community'
#
# urlpatterns = [
#     path('write/', CommunityWriteView.as_view(), name='community-write'),
#     path('list/', CommunityListView.as_view(), name='community-list'),
#     path('detail/', CommunityDetailView.as_view(), name='community-detail')
# ]



from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from community.views import CommunityWriteView, CommunityDetailView, CommunityListView, CommunityDeleteView, \
    CommunityUpdateView


app_name = 'community'

urlpatterns = [
    path('write/', CommunityWriteView.as_view(), name='write'),
    path('detail/', CommunityDetailView.as_view(), name='detail'),
    path('list/', CommunityListView.as_view(), name='list'),
    path('delete/', CommunityDeleteView.as_view(), name='delete'),
    path('update/', CommunityUpdateView.as_view(), name='update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)