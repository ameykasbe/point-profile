from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from . import github as gh


def input(request):
    return render(request, 'dashboards/input.html')


def profile_analysis(request):
    if request.method == 'POST':
        user = request.POST.get('userid')
    else:
        return redirect('input')
    projects_per_languages, lang_distribution, repos_info = gh.get_repo_data(
        user)
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

    # User info
    user_info_response = gh.get_user_info(user)
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
        'repos_info': repos_info_sorted_stars,
    }
    return render(request, 'dashboards/profile-analysis.html', context)
