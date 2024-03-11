from rest_framework.response import Response
from rest_framework.views import APIView

from reply.models import Reply


class ReplyWriteAPI(APIView):
    def post(self, request):
        # 1. FormData객체가 들어오는 가
        # request.POST

        # 2. JSON이 들어오는 가
        data = request.data
        data = {
            'reply_content': data['reply_content'],
            'community_id': data['community_id'],
            'member_id': request.session['member']['id']
        }

        Reply.objects.create(**data)
        return Response('success')