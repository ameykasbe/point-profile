from django.shortcuts import render
from django.http import HttpResponse
from . import github as gh


def profile_analysis(request):
    user = "anamayasarvate"
    projects_per_language = gh.projects_per_languages(user)    
    languages = [key for key in projects_per_language]
    num_projects = [value for key, value in projects_per_language.items()]

    context = {
        'languages' : languages,
        'num_projects': num_projects,
    }
    return render(request, 'dashboards/profile-analysis.html', context)