from django.db import models

# Create your models here.

class ServiceData(models.Model):
    fileName = models.CharField(max_length = 1000000)
    test = models.BooleanField(null = False, default=True)
    # file = models.BinaryField(max_length=100000, default = bytes(100000))
    
