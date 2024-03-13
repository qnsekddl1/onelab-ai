from django.urls import path

from school.views import SchoolMainView

app_name = 'school'

urlpatterns = [
    path('main/', SchoolMainView.as_view(), name='main'),
]
