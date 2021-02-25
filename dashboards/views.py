from django.shortcuts import render
from django.http import HttpResponse

def profile_analysis(request):
    return render(request, 'dashboards/profile-analysis.html')