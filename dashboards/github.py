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
        return e
    response_text_dict = json.loads(response.text)
    return response_text_dict


def get_languages_data(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    """Returns a dictionary with all the languages used by a user with key as the language and value as the percentage of code written."""
    # url = "https://api.github.com/users/" + user + "/repos"
    # repos = get_response_text_dict(url)
    # if type(repos) == list:  # If no error occured.
    #     languages_list = list()
    #     for repo in repos:
    #         languages_url = repo.get('languages_url')
    #         languages = get_response_text_dict(languages_url)
    #         languages_list.append(languages)
    #     repos_languages = languages_list
    # else:
    #     repos_languages = repos  # If error occurs, repos_language contains error message

    # Format - repos_languages = [
    #     {'JavaScript': 94325, 'CSS': 7750, 'HTML': 821},
    #     {'Python': 10055, 'HTML': 4771, 'CSS': 274},
    #     {'HTML': 3499, 'Python': 2712},
    #     {'CSS': 202283, 'JavaScript': 100300, 'HTML': 40012, 'Python': 23442},
    #     {'Python': 11083},
    #     {'Python': 15386, 'HTML': 12253, 'CSS': 1125},
    #     {'Python': 9788, 'HTML': 2983},
    #     {'Python': 7717, 'HTML': 3384}
    # ]

    # if type(repos_languages) == list:
    #     projects_per_languages = dict()
    #     languages_distribution = dict()
    #     for repo in repos_languages:
    #         for (language, bytes_lang) in repo.items():
    #             if language in projects_per_languages:
    #                 projects_per_languages[language] += 1
    #             else:
    #                 projects_per_languages[language] = 1

    #             if language in languages_distribution:
    #                 languages_distribution[language] += bytes_lang
    #             else:
    #                 languages_distribution[language] = bytes_lang
    #     return projects_per_languages, languages_distribution
    # return repos_languages

    projects_per_languages = {'JavaScript': 2,
                              'CSS': 4, 'HTML': 7, 'Python': 7}
    languages_distribution = {'JavaScript': 194625,
                              'CSS': 211432, 'HTML': 67723, 'Python': 80183}
    return projects_per_languages, languages_distribution


def get_user_info(user):
    """Returns user information."""
    # url = "https://api.github.com/users/" + user
    # user_info_response = get_response_text_dict(url)
    user_info_response = {
        'login': 'anamayasarvate',
        'id': 47415511,
        'node_id': 'MDQ6VXNlcjQ3NDE1NTEx',
        'avatar_url': 'https://avatars.githubusercontent.com/u/47415511?v=4',
        'gravatar_id': '',
        'url': 'https://api.github.com/users/anamayasarvate',
        'html_url': 'https://github.com/anamayasarvate',
        'followers_url': 'https://api.github.com/users/anamayasarvate/followers',
        'following_url': 'https://api.github.com/users/anamayasarvate/following{/other_user}',
        'gists_url': 'https://api.github.com/users/anamayasarvate/gists{/gist_id}',
        'starred_url': 'https://api.github.com/users/anamayasarvate/starred{/owner}{/repo}',
        'subscriptions_url': 'https://api.github.com/users/anamayasarvate/subscriptions',
        'organizations_url': 'https://api.github.com/users/anamayasarvate/orgs',
        'repos_url': 'https://api.github.com/users/anamayasarvate/repos',
        'events_url': 'https://api.github.com/users/anamayasarvate/events{/privacy}',
        'received_events_url': 'https://api.github.com/users/anamayasarvate/received_events',
        'type': 'User',
        'site_admin': False,
        'name': 'Anamay Sarvate',
        'company': None,
        'blog': 'www.anamaysarvate.com',
        'location': None,
        'email': None,
        'hireable': None,
        'bio': 'Python/Django and MERN stack developer',
        'twitter_username': None,
        'public_repos': 12,
        'public_gists': 0,
        'followers': 0,
        'following': 0,
        'created_at': '2019-02-07T09:49:37Z',
        'updated_at': '2021-03-09T15:06:51Z'}

    return user_info_response
