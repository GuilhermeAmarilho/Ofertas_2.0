import os, requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
GOOGLE_SEARCH_API_ENGINE = os.getenv('GOOGLE_SEARCH_API_ENGINE')


def searchIMG(query, qt=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_SEARCH_API_KEY,
        "cx": GOOGLE_SEARCH_API_ENGINE,
        "q": query,
        "searchType": "image",
        "num": qt,
        "fileType": "png"
    }
    results = []
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            dados = response.json()
            # print('\n\n\n\n\n')
            for item in dados.get("items"):
                if item.get("fileFormat") == "image/png":
                    results.append(item.get("link"))
            return results
        except:
            return []
