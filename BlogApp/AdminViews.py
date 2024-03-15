from django.shortcuts import render


def admin_base(request):
    return render(request,'adminDashboard/admin_base.html')