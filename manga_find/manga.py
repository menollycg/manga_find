"""
    Manga API access
"""
import requests

url = "https://api.consumet.org/manga/mangadex/{}"


def look_up(question: str) -> list:
    """ Look_up takes a string question and returns a list.
    Question is the search term(s) for the manga the user is attempting to look up.
    If no results, a type error might be thrown.
    :param question:
    :return:
    """
    send_url = url.format(question)
    response = requests.get(send_url)
    data = response.json()
    results = data['results']
    return results
