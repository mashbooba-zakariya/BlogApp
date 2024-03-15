from django.shortcuts import render


def audience_base(request):
    return render(request,'AudienceDashboard/audience_base.html')