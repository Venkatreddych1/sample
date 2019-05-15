from django.db import models
from datetime import datetime

class Reg(models.Model):
    email=models.CharField(max_length=100)
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    date=models.DateTimeField(default=datetime.now,blank=True)
    file=models.FileField()
    comment=models.CharField(max_length=200)
