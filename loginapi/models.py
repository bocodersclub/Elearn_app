from django.db import models

# Create your models here.

class dbinfo(models.Model):
    subjectname=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    
