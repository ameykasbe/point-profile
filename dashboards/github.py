import requests
import json

username = 'ameykasbe'
token = 'a5a027f83aa8227d835a7d7fcd408ed99d8ab9b8'

def get_response_text_dict(url):
	"""Returns the response content of the GET request of a url in a dictionary format."""
	response = requests.get(url, auth=(username, token))
	try:
		response.raise_for_status()
	except Exception as e:
		return e
	response_text_dict = json.loads(response.text)
	return response_text_dict


def get_languages(user):
    """Returns a list of dictionaries of languages corresponding to different repositories of a user."""

    # repos_languages = [{'JavaScript': 94325, 'CSS': 7750, 'HTML': 821}, {'Python': 10055, 'HTML': 4771, 'CSS': 274}, {'HTML': 3499, 'Python': 2712}, {'CSS': 202283, 'JavaScript': 100300, 'HTML': 40012, 'Python': 23442}, {'Python': 11083}, {'Python': 15386, 'HTML': 12253, 'CSS': 1125}, {'Python': 9788, 'HTML': 2983}, {'Python': 7717, 'HTML': 3384}]
    # return repos_languages

    # url = "https://api.github.com/users/" + user + "/repos"
    # repos = get_response_text_dict(url)
    # if type(repos) == list: # If no error occured.
    #     languages_list = list()
    #     for repo in repos:
    #         languages_url = repo.get('languages_url')
    #         languages = get_response_text_dict(languages_url)
    #         languages_list.append(languages)
    #     return languages_list
    languages_list = [
            {'JavaScript': 94325, 'CSS': 7750, 'HTML': 821}, 
            {'Python': 10055, 'HTML': 4771, 'CSS': 274}, 
            {'HTML': 3499, 'Python': 2712}, 
            {'CSS': 202283, 'JavaScript': 100300, 'HTML': 40012, 'Python': 23442}, 
            {'Python': 11083}, 
            {'Python': 15386, 'HTML': 12253, 'CSS': 1125}, 
            {'Python': 9788, 'HTML': 2983}, 
            {'Python': 7717, 'HTML': 3384}
        ]
    return languages_list
    return repos # If error occured, return the error.


def projects_per_languages(user):
    """Returns a dictionary with all the languages used by a user with key as the language and value as the number of projects."""
    repos_languages = get_languages(user)
    languages = dict()
    for repo in repos_languages:
        for (language,bytes_lang) in repo.items():
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    return languages
    # languages = {'JavaScript': 2, 'CSS': 4, 'HTML': 7, 'Python': 7}
