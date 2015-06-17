#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper  
import mimetypes  
from colsite import settings  
import os 

from django.http import HttpResponse
 
# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临!")

def home(request):
    return render(request, 'home.html')

def company(request):
    return render_to_response('company.html',{})

def start(request):
    return render_to_response('start.html',{})

def file_download(request, filename):  
    filepath = os.path.join(settings.Download_file, filename)    
    wrapper = FileWrapper(open(filepath, 'rb'))  
    content_type = mimetypes.guess_type(filepath)[0]  
    response = HttpResponse(wrapper, content_type = content_type)  
    response['Content-Disposition'] = "attachment; filename=%s" % filename  
    return response    

def test(request):
    return render(request, 'test.html')

