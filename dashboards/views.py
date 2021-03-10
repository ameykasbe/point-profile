from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import github as gh


def profile_analysis(request):
    user = "anamayasarvate"
    projects_per_languages, lang_distribution = gh.get_languages_data(
        user)

    # Projects per languages
    languages = [key for key in projects_per_languages]
    num_projects = [value for key, value in projects_per_languages.items()]

    # Language distribution
    languages_distribution = [key for key in lang_distribution]
    bytes_per_language = [value for key,
                          value in lang_distribution.items()]

    # User info
    user_info_response = gh.get_user_info(user)
    user_info = dict()
    user_info['name'] = user_info_response.get('name')
    user_info['email'] = user_info_response.get('email')
    user_info['company'] = user_info_response.get('company')
    user_info['location'] = user_info_response.get('location')
    user_info['github_id'] = '@' + user_info_response.get('login')
    user_info['avatar_url'] = user_info_response.get('avatar_url')
    user_info['html_url'] = user_info_response.get('html_url')
    user_info['bio'] = user_info_response.get('bio')
    created_at = user_info_response.get('created_at')
    # Format = '2019-02-07T09:49:37Z'
    created_at = datetime.datetime.fromisoformat(created_at[:-1])
    # Format = datetime.datetime(2019, 2, 7, 9, 49, 37)
    user_info['created_at'] = created_at.date()
    # Format = datetime.datetime(2019, 2, 7)
    context = {
        'languages': languages,
        'num_projects': num_projects,
        'languages_distribution': languages_distribution,
        'bytes_per_language': bytes_per_language,
        'user_info': user_info
    }
    return render(request, 'dashboards/profile-analysis.html', context)
