from django.db import models
from datetime import datetime

class Reg(models.Model):
    email=models.CharField(max_length=100)
    user = models.CharField(max_length=30)
    pwd = models.CharField(max_length=20)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    date=models.DateTimeField(default=datetime.now,blank=True)
    location=models.PointField()
    file=models.FileField()
    comment=models.TextField()
