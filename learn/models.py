from django.db import models

# Create your models here.
class UploadFile(models.Model):
    username=models.CharField(max_length=50)
    uploadfile=models.FileField(upload_to='./learn/static/uploadfile') 
    
    def __unicode__(self):
        return self.username
