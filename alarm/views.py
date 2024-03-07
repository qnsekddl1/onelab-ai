from django.shortcuts import render
from django.views import View


class AlarmDetailView(View):
    def get(self, request):
        return render(request, 'alarm/alarm.html')
