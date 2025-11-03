from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from .models import Candidate

# Create your views here.

class ApiView(ListView):
    
    def get(self,request):
        return HttpResponse('GET method: SUCCESS')
    
    
    def post(self,request):
        return HttpResponse('POST method: SUCCESS')


def api_views(request):
    return HttpResponse('SUCCESS****')

@csrf_exempt
def api_post(request):
    if request.method == 'POST':
        print(f'POST method',request.FILES.get('file'))
        file = request.FILES.get('file')
        print(f'file is {file},{type(file)}')
        record = Candidate(1001,"Abhi",'Kakolla','ml engineer',file)
        record.save()
    else:
        print('NOT A POST METHOD******')
    return HttpResponse('FILE UPLOADED',"CV is saved to Datbase SUCCESSFULLY")