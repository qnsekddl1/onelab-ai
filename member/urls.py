from django.urls import path

from member.views import MemberJoinView, MemberCheckIdView, MemberLoginView, SendVerificationCodeView, \
    MemberNormalJoinView, MemberIdSearchView, MemberResetPasswordView, MemberActivateEmailView, MemberMainView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('join-normal/', MemberNormalJoinView.as_view(), name='join-normal'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('check-id/', MemberCheckIdView.as_view(), name='check-id'),
    path('activate/<str:school>', SendVerificationCodeView.as_view(), name='activate'),
    path('account-find/', MemberIdSearchView.as_view(), name='account-find'),
    path('account-activate/<str:email>', MemberActivateEmailView.as_view(), name='account-activate'),
    path('account-reset/<int:id>/<str:random>/',MemberResetPasswordView.as_view(), name='account-reset'),
]
