from django.db import models

# Create your models here.


class User(models.Model):
    '''定义用户类'''
    name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='app01')