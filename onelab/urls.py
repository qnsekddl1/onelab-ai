from django.urls import path

from onelab.views import OneLabWriteView, OneLabListView, OneLabDetailView

app_name = 'onelab'

urlpatterns = [
    path('write/', OneLabWriteView.as_view(), name='one-lab-write'),
    path('list/', OneLabListView.as_view(), name='one-lab-list'),
    path('detail/', OneLabDetailView.as_view(), name='one-lab-detail')
]