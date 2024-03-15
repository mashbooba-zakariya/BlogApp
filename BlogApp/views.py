from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from BlogApp.forms import LoginRegister, AudienceRegister, BloggerRegister


# Create your views here.

def base(request):
    return render(request,'base.html')


def index(request):
    return render(request,'index.html')



#----------Audience Registration form function------------

def Audience_Register(request):
    login_register = LoginRegister()
    audience_register = AudienceRegister()


    if request.method == 'POST':
        user1 = LoginRegister(request.POST)
        user2 = AudienceRegister(request.POST)

        if user1.is_valid() and user2.is_valid():
            form = user1.save(commit = False)
            form.is_audience = True
            form.save()

            data = user2.save(commit = False)
            data.user = form
            data.save()

            return redirect('LoginPage')
    return render(request, 'AudienceRegister.html',{'audience_register':audience_register,'login_register':login_register})


#----------Blogger Registration form function-----------

def Blogger_Register(request):
    login_register = LoginRegister()
    blogger_register = BloggerRegister()


    if request.method == 'POST':
        user1 = LoginRegister(request.POST)
        user2 = BloggerRegister(request.POST, request.FILES)

        if user1.is_valid() and user2.is_valid():
            form = user1.save(commit=False)
            form.is_blogger = True
            form.save()

            data = user2.save(commit=False)
            data.user = form
            data.save()

            return redirect('LoginPage')
    return render(request,'BloggerRegister.html',{'login_register':login_register,'blogger_register':blogger_register})


#--------Login form function--------

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)


        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_base')
            elif user.is_audience:
                return redirect('audience_base')
            elif user.is_blogger:
                return redirect('blogger_base')

        else:
            messages.info(request,"User not found")

    return render(request,'LoginPage.html')


