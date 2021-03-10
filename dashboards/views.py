from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import github as gh


def profile_analysis(request):
    user = "anamayasarvate"
    projects_per_languages, lang_distribution, repos_info = gh.get_repo_data(
        user)

    if type(projects_per_languages) == list:
        # Projects per languages
        languages = [key for key in projects_per_languages]
        num_projects = [value for key, value in projects_per_languages.items()]

    if type(lang_distribution) == list:
        # Language distribution
        languages_distribution = [key for key in lang_distribution]
        bytes_per_language = [value for key,
                              value in lang_distribution.items()]

    if type(repos_info) == list:
        for repo in repos_info:
            repo['size'] = str(repo['size']) + ' kB'

        # User info
    user_info_response = gh.get_user_info(user)
    if type(user_info_response) == list:
        user_info_response['github_id'] = '@' + user_info_response.get('login')
        created_at = user_info_response.get('created_at')
        created_at = datetime.datetime.fromisoformat(created_at[:-1])
        user_info_response['created_at'] = created_at.date()

    context = {
        'languages': languages,
        'num_projects': num_projects,
        'languages_distribution': languages_distribution,
        'bytes_per_language': bytes_per_language,
        'user_info': user_info_response,
        'repos_info': repos_info,
    }
    return render(request, 'dashboards/profile-analysis.html', context)
