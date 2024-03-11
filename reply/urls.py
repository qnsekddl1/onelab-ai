from django.urls import path


from reply.views import ReplyWriteAPI

app_name = 'replies'

urlpatterns = [
    path('write/', ReplyWriteAPI.as_view(), name='write'),
]
