from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class ApiView(View):
    
    def get(self,request):
        return HttpResponse('GET method: SUCCESS')
    
    
    def post(self,request):
        return HttpResponse('POST method: SUCCESS')


def api_views(request):
    return HttpResponse('SUCCESS****')