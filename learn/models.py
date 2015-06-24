from django.db import models

# Create your models here.
class UploadFile(models.Model):
    uploadfile=models.FileField(upload_to='./learn/static/uploadfile') 
    
