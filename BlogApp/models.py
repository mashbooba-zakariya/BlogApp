import datetime
from datetime import timezone

from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models



class Login(AbstractUser):
    is_blogger = models.BooleanField(default=False)
    is_audience = models.BooleanField(default=False)


class Blogger(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='Blog_user')
    name = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    bio = models.CharField(max_length=50, null=True, blank=True)


class Audience(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)




# -------Blog Creation model-----------


class CreateBlog(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='document/')
    published_date = models.DateTimeField()



