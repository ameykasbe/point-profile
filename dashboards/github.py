import requests
import json
import pathlib

username = 'ameykasbe'
token = 'a5a027f83aa8227d835a7d7fcd408ed99d8ab9b8'


def get_json(response):
    """Returns the dictionary of the response object."""
    response_text_dict = json.loads(response.text)
    return response_text_dict


def check_limit():
    response = requests.get("https://api.github.com/rate_limit")
    try:
        response.raise_for_status()
    except Exception:
        return None, None
    json_response = get_json(response)
    limit = json_response.get('resources').get('core').get('limit')
    remaining = json_response.get('resources').get('core').get('remaining')
    return limit, remaining


def get_user_info(user):
    """Returns user information."""
    url = "https://api.github.com/users/" + user
    response = requests.get(url)
    return response


def get_repo_data(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    """Returns a dictionary with all the languages used by a user with key as the language and value as the percentage of code written."""

    url = "https://api.github.com/users/" + user + "/repos"
    response = requests.get(url)

    # file_path = pathlib.Path(__file__).parent / 'repos_data.json'
    # with open(file_path, 'r') as filename:
    #     repo_response = json.load(filename)

    return response

    # projects_per_languages = {'JavaScript': 2,
    #                           'CSS': 4, 'HTML': 7, 'Python': 7}
    # languages_distribution = {'JavaScript': 194625,
    #                           'CSS': 211432, 'HTML': 67723, 'Python': 80183}
    # return projects_per_languages, languages_distribution, repos_info
