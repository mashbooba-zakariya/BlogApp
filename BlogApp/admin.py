from django.contrib import admin

from BlogApp import models

# Register your models here.

admin.site.register(models.Login)
admin.site.register(models.Blogger)
admin.site.register(models.Audience)
admin.site.register(models.CreateBlog)