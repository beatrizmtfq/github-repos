import requests


def get_users(username):
    url = f"https://api.github.com/users/%7Busername%7D/repos"
    response = requests.get(url)
    return response.json()

