from django.urls import path
from BlogApp import views, BlogCreatorViews, AudienceViews, AdminViews

urlpatterns = [
    path('',views.index,name='index'),
    path('base', views.base, name='base'),


# Login and Registration
    path('LoginPage',views.LoginPage,name='LoginPage'),
    path('Audience_Register',views.Audience_Register,name='Audience_Register'),
    path('Blogger_Register',views.Blogger_Register,name='Blogger_Register'),

#  -------------------Admin Pages---------------------
    path('admin_base', AdminViews.admin_base, name='admin_base'),







# -------------Audience Pages---------------------
    path('audience_base',AudienceViews.audience_base,name='audience_base'),







    # ---------------Blogger Pages---------------------------
    path('blogger_base', BlogCreatorViews.blogger_base, name='blogger_base'),
    path('CreateBlogs',BlogCreatorViews.CreateBlogs,name='CreateBlogs')
]