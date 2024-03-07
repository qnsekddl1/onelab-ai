from django.urls import path

from alarm.views import AlarmDetailView


app_name = 'alarm'

urlpatterns = [
    path('detail/', AlarmDetailView.as_view(), name='alarm-detail'),
]