from django.conf.urls.static import static
from django.urls import path

from myPage.views import MyPageMainView, MyPagePointView, DeleteProfileView, MyPageCommunityView, MemberLogoutView, \
    MyPagePlaceAPIView
from oneLabProject import settings

app_name = 'myPage'
urlpatterns = [
    path('main/',MyPageMainView.as_view(),name='main'),
    path('main/<int:page>/',MyPagePlaceAPIView.as_view(),name='main'),
    path('main/delete/',DeleteProfileView.as_view(),name='delete'),
    path('my_point/',MyPagePointView.as_view(), name='mypage_point'),
    path('community/',MyPageCommunityView.as_view(), name='community'),
    path('logout/',MemberLogoutView.as_view(),name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
