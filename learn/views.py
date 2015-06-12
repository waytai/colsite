#coding:utf-8
from django.shortcuts import render
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

def test(request):
    return render(request, 'test.html')

def file_download(request, filename):  
    filepath = os.path.join(settings.Download_file, filename)    
    wrapper = FileWrapper(open(filepath, 'rb'))  
    content_type = mimetypes.guess_type(filepath)[0]  
    response = HttpResponse(wrapper, content_type = content_type)  
    response['Content-Disposition'] = "attachment; filename=%s" % filename  
    return response    
