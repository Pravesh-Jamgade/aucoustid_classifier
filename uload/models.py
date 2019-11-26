from django.db import models

# Create your models here.

class UploadMedia(models.Model):
    uploaded_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    test = models.BooleanField(default=False)

