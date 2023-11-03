""" A Manga Discovery Tool

"""

import requests

if __name__ == "__main__":

    response = requests.get("https://api.consumet.org/manga/mangadex/demon")

    demon_manga = response.json()

    for result in demon_manga["results"]:
        print(result["title"])
