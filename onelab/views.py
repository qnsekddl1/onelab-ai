from django.shortcuts import render
from django.views import View


class OneLabWriteView(View):
    def get(self, request):
        return render(request, 'onelab/one-lab-write.html')

class OneLabListView(View):
    def get(self, request):
        return render(request, 'onelab/one-lab-list.html')

class OneLabDetailView(View):
    def get(self, request):
        return render(request, 'onelab/one-lab-detail.html')