"""colsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url  
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'learn.views.company', name='company'), 
    url(r'^test$', 'learn.views.test', name='test'), 
    url(r'^home/', 'learn.views.home', name='home_value'), 
    url(r'^index/', 'learn.views.index', name='index'), 
    url(r'^start$', 'learn.views.start', name='start'), 
    url(r'^login$', 'learn.views.login', name='login'), 
    url(r'^manage$', 'learn.views.manage', name='manage'), 
    url(r'^upload_file$', 'learn.views.upload_file', name='upload_file'), 
    url(r'^admin/', include(admin.site.urls)),
    url('^download/filename=(?P<filename>.{1,500})/$', 'learn.views.file_download', name='download'),
]
