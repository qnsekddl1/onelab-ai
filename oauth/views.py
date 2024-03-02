from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render
from django.views import View


class OAuthLoginView(View):
    def get(self, request):
        user = SocialAccount.objects.get(user=request.user)
        print(user.provider)
        print(user.extra_data)
        # 메인으로 가도록 변경해야함
        # return render(request, 'member/login.html')
        return render(request, '/')