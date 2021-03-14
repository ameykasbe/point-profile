import requests
import json
import pathlib

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
    return response_text_dict, response.headers


def get_repo_data(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    """Returns a dictionary with all the languages used by a user with key as the language and value as the percentage of code written."""

    url = "https://api.github.com/users/" + user + "/repos"
    repo_response, headers = get_response_text_dict(url)

    # file_path = pathlib.Path(__file__).parent / 'repos_data.json'
    # with open(file_path, 'r') as filename:
    #     repo_response = json.load(filename)
    repos_languages = list()
    repos_info = list()
    for repo in repo_response:
        languages_url = repo.get('languages_url')
        languages, headers = get_response_text_dict(languages_url)
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
    return projects_per_languages, languages_distribution, repos_info, headers

    # projects_per_languages = {'JavaScript': 2,
    #                           'CSS': 4, 'HTML': 7, 'Python': 7}
    # languages_distribution = {'JavaScript': 194625,
    #                           'CSS': 211432, 'HTML': 67723, 'Python': 80183}
    # return projects_per_languages, languages_distribution, repos_info


def get_user_info(user):
    """Returns user information."""
    url = "https://api.github.com/users/" + user
    user_info_response, headers = get_response_text_dict(url)
    # file_path = pathlib.Path(__file__).parent / 'user_info.json'
    # with open(file_path, 'r') as filename:
    #     user_info_response = json.load(filename)
    return user_info_response, headers
