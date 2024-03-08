from django.urls import path

from member.views import MemberJoinView, MemberCheckIdView, MemberLoginView, SendVerificationCodeView, MemberMainView, \
    MemberNormalJoinView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('join-normal/', MemberNormalJoinView.as_view(), name='join-normal'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('check-id/', MemberCheckIdView.as_view(), name='check-id'),
    path('activate/', SendVerificationCodeView.as_view(), name='activate'),
    path('main/', MemberMainView.as_view(), name='main')
]
