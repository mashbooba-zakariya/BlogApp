from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from BlogApp.forms import CreateBlogForm
from BlogApp.models import CreateBlog


def blogger_base(request):
    return render(request,'BlogCreatorDashboard/blogger_base.html')


# ---------- create blogs----------

def CreateBlogs(request):
    form = CreateBlogForm()
    if request.method == 'POST':
        data = CreateBlogForm(request.POST, request.FILES)
        if data.is_valid():
            title = data.cleaned_data['title']
            content = data.cleaned_data['content']
            image = data.cleaned_data['image']
            CreateBlog.objects.create(user=request.user,title=title,content=content,image=image,published_date=datetime.now())
            messages.info(request, ' added succesfully')
            return redirect('blogger_base')
        else:
            messages.info(request, 'Form submission failed. Please check your inputs.')
    return render(request,'BlogCreatorDashboard/CreateBlogs.html',{'form':form})