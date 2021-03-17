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
    return response_text_dict


def check_limit():
    response = get_response_text_dict("https://api.github.com/rate_limit")
    limit = response.get('resources').get('core').get('limit')
    remaining = response.get('resources').get('core').get('remaining')
    return limit, remaining


def get_repo_data(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    """Returns a dictionary with all the languages used by a user with key as the language and value as the percentage of code written."""

    url = "https://api.github.com/users/" + user + "/repos"
    repo_response = get_response_text_dict(url)

    # file_path = pathlib.Path(__file__).parent / 'repos_data.json'
    # with open(file_path, 'r') as filename:
    #     repo_response = json.load(filename)

    return repo_response

    # projects_per_languages = {'JavaScript': 2,
    #                           'CSS': 4, 'HTML': 7, 'Python': 7}
    # languages_distribution = {'JavaScript': 194625,
    #                           'CSS': 211432, 'HTML': 67723, 'Python': 80183}
    # return projects_per_languages, languages_distribution, repos_info


def get_user_info(user):
    """Returns user information."""
    url = "https://api.github.com/users/" + user
    user_info_response = get_response_text_dict(url)
    # file_path = pathlib.Path(__file__).parent / 'user_info.json'
    # with open(file_path, 'r') as filename:
    #     user_info_response = json.load(filename)
    return user_info_response
