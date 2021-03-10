import requests
import json

username = 'ameykasbe'
token = 'a5a027f83aa8227d835a7d7fcd408ed99d8ab9b8'


def get_response_text_dict(url):
    """Returns the response content of the GET request of a url in a dictionary format."""
    response = requests.get(url)
    # response = requests.get(url, auth=(username, token))
    try:
        response.raise_for_status()
    except Exception as e:
        print(e)
    response_text_dict = json.loads(response.text)
    return response_text_dict


def get_repo_data(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    """Returns a dictionary with all the languages used by a user with key as the language and value as the percentage of code written."""

    url = "https://api.github.com/users/" + user + "/repos"
    repo_response = get_response_text_dict(url)

    repos_languages = list()
    repos_info = list()
    for repo in repo_response:
        languages_url = repo.get('languages_url')
        languages = get_response_text_dict(languages_url)
        repos_languages.append(languages)

        repo_info = dict()
        repo_info['html_url'] = repo.get('html_url')
        repo_info['description'] = repo.get('description')
        repo_info['name'] = repo.get('name')
        repo_info['language'] = repo.get('language')
        repo_info['size'] = repo.get('size')
        repos_info.append(repo_info)

    projects_per_languages = dict()
    languages_distribution = dict()
    for repo in repos_languages:
        for (language, bytes_lang) in repo.items():
            if language in projects_per_languages:
                projects_per_languages[language] += 1
            else:
                projects_per_languages[language] = 1

            if language in languages_distribution:
                languages_distribution[language] += bytes_lang
            else:
                languages_distribution[language] = bytes_lang
    return projects_per_languages, languages_distribution, repos_info

    # projects_per_languages = {'JavaScript': 2,
    #                           'CSS': 4, 'HTML': 7, 'Python': 7}
    # languages_distribution = {'JavaScript': 194625,
    #                           'CSS': 211432, 'HTML': 67723, 'Python': 80183}
    # return projects_per_languages, languages_distribution, repos_info


def get_user_info(user):
    """Returns user information."""
    url = "https://api.github.com/users/" + user
    user_info_response = get_response_text_dict(url)
    # user_info_response = {
    #     'login': 'anamayasarvate',
    #     'id': 47415511,
    #     'node_id': 'MDQ6VXNlcjQ3NDE1NTEx',
    #     'avatar_url': 'https://avatars.githubusercontent.com/u/47415511?v=4',
    #     'gravatar_id': '',
    #     'url': 'https://api.github.com/users/anamayasarvate',
    #     'html_url': 'https://github.com/anamayasarvate',
    #     'followers_url': 'https://api.github.com/users/anamayasarvate/followers',
    #     'following_url': 'https://api.github.com/users/anamayasarvate/following{/other_user}',
    #     'gists_url': 'https://api.github.com/users/anamayasarvate/gists{/gist_id}',
    #     'starred_url': 'https://api.github.com/users/anamayasarvate/starred{/owner}{/repo}',
    #     'subscriptions_url': 'https://api.github.com/users/anamayasarvate/subscriptions',
    #     'organizations_url': 'https://api.github.com/users/anamayasarvate/orgs',
    #     'repos_url': 'https://api.github.com/users/anamayasarvate/repos',
    #     'events_url': 'https://api.github.com/users/anamayasarvate/events{/privacy}',
    #     'received_events_url': 'https://api.github.com/users/anamayasarvate/received_events',
    #     'type': 'User',
    #     'site_admin': False,
    #     'name': 'Anamay Sarvate',
    #     'company': None,
    #     'blog': 'www.anamaysarvate.com',
    #     'location': None,
    #     'email': None,
    #     'hireable': None,
    #     'bio': 'Python/Django and MERN stack developer',
    #     'twitter_username': None,
    #     'public_repos': 12,
    #     'public_gists': 0,
    #     'followers': 0,
    #     'following': 0,
    #     'created_at': '2019-02-07T09:49:37Z',
    #     'updated_at': '2021-03-09T15:06:51Z'}
    return user_info_response
