#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.servers.basehttp import FileWrapper  
from django.template import RequestContext
from models import UploadFile
import mimetypes  
from colsite import settings  
import os 
from forms import UploadFileForm
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
 
# Create your views here.
def index(request):
    return HttpResponse(u"欢迎光临!")

def home(request):
    return render(request, 'home.html')

def mylogin(request):
    global username
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user) 
        return render_to_response('manage.html', {'username': username}, context_instance=RequestContext(request))
    return render(request, 'login.html')

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

def manage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile=form.cleaned_data['uploadfile']
            u=UploadFile()
            u.uploadfile=uploadfile
            u.save()
            return render_to_response('manage.html', {'username': username, 'form': form},context_instance=RequestContext(request))
    else:
        form = UploadFileForm()
    return render_to_response('manage.html', {'username': username},context_instance=RequestContext(request))

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #username=form.cleaned_data['username']
            uploadfile=form.cleaned_data['uploadfile']
            u=UploadFile()
            #u.username=username
            u.uploadfile=uploadfile
            u.save()
            return HttpResponse('OK')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form},  context_instance=RequestContext(request))

