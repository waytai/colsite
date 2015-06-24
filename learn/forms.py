#########################################################################
# -*- coding:utf-8 -*- 
# File Name: forms.py
# Author: wayne
# mail: @163.com
# Created Time: 2015/6/19 14:21:46
#########################################################################
#!/bin/python
from django import forms
 
class UploadFileForm(forms.Form):
    uploadfile = forms.FileField()
