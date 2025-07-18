import os, requests
from dotenv import load_dotenv

load_dotenv()
GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
GOOGLE_SEARCH_API_ENGINE = os.getenv('GOOGLE_SEARCH_API_ENGINE')

def buscar_google(consulta, quantidade=5):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_SEARCH_API_KEY,
        "cx": GOOGLE_SEARCH_API_ENGINE,
        "q": consulta,
        "searchType": "image",
        "num": quantidade
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        dados = response.json()
        imagens = [item['link'] for item in dados.get("items", [])]
        return imagens
    else:
        print("Erro:", response.status_code)
        print(response.text)
        return []
    