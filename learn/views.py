#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临!")

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')
