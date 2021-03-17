from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from . import github as gh
import requests


def input(request):
    limit, remaining = gh.check_limit()
    if limit == None and remaining == None:
        context = {
            'error_message': 'Something went wrong. Please try again later!'
        }
        return render(request, 'dashboards/error-page.html', context)
    context = {
        'limit': limit,
        'remaining': remaining
    }
    return render(request, 'dashboards/input.html', context)


def profile_analysis(request):
    if request.method == 'POST':
        user = request.POST.get('userid')
    else:
        return redirect('input')

    # User info
    response = gh.get_user_info(user)
    try:
        response.raise_for_status()
    except Exception:
        limit, remaining = gh.check_limit()
        if remaining == 0:
            context = {
                'error_message': 'Requests limit reached. Please try again later!'
            }
        else:
            context = {
                'error_message': 'User Not Found!1'
            }
        return render(request, 'dashboards/error-page.html', context)

    user_info_response = gh.get_json(response)
    user_info_response['github_id'] = '@' + user_info_response.get('login')
    created_at = user_info_response.get('created_at')
    created_at = datetime.datetime.fromisoformat(created_at[:-1])
    user_info_response['created_at'] = created_at.date()

    # Repository information
    response = gh.get_repo_data(user)
    try:
        response.raise_for_status()
    except Exception:
        limit, remaining = gh.check_limit()
        if remaining == 0:
            context = {
                'error_message': 'Requests limit reached. Please try again later!'
            }
        else:
            context = {
                'error_message': 'Something went wrong. Please try again later!'
            }
        return render(request, 'dashboards/error-page.html', context)

    repo_response = gh.get_json(response)
    repos_languages = list()
    repos_info = list()
    for repo in repo_response:
        languages_url = repo.get('languages_url')
        res = requests.get(languages_url)
        languages = gh.get_json(res)
        repos_languages.append(languages)

        repo_info = dict()
        repo_info['html_url'] = repo.get('html_url')
        repo_info['description'] = repo.get('description')
        repo_info['name'] = repo.get('name')
        repo_info['language'] = repo.get('language')
        repo_info['size'] = repo.get('size')
        repo_info['stargazers_count'] = repo.get('stargazers_count')
        repos_info.append(repo_info)

    projects_per_languages = dict()
    lang_distribution = dict()
    for repo in repos_languages:
        for (language, bytes_lang) in repo.items():
            if language in projects_per_languages:
                projects_per_languages[language] += 1
            else:
                projects_per_languages[language] = 1

            if language in lang_distribution:
                lang_distribution[language] += bytes_lang
            else:
                lang_distribution[language] = bytes_lang

    # Projects per languages
    languages = [key for key in projects_per_languages]
    num_projects = [value for key, value in projects_per_languages.items()]

    # Language distribution
    languages_distribution = [key for key in lang_distribution]
    bytes_per_language = [value for key,
                          value in lang_distribution.items()]

    repos_info_sorted_stars = sorted(
        repos_info, key=lambda repo: repo.get('stargazers_count'), reverse=True)
    if len(repos_info_sorted_stars) > 6:
        repos_info_sorted_stars = repos_info_sorted_stars[:6]
    for repo in repos_info_sorted_stars:
        repo['size'] = str(repo['size']) + ' kB'
        if len(repo.get('description')) > 100:
            repo['description'] = repo['description'][:101] + '...'

    limit, remaining = gh.check_limit()

    context = {
        'languages': languages,
        'num_projects': num_projects,
        'languages_distribution': languages_distribution,
        'bytes_per_language': bytes_per_language,
        'user_info': user_info_response,
        'repos_info': repos_info_sorted_stars,
        'limit': limit,
        'remaining': remaining
    }
    return render(request, 'dashboards/profile-analysis.html', context)


# TODO
# Limit check
