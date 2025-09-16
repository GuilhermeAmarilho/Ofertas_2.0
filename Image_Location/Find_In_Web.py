import os, requests
from PIL import Image
from io import BytesIO
from pathlib import Path
from dotenv import load_dotenv

path = Path("\\".join(os.path.abspath(__file__).split('\\')[:(-2)])+'\\.env')
load_dotenv(path, override=True)
GOOGLE_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
GOOGLE_SEARCH_API_ENGINE = os.getenv('GOOGLE_SEARCH_API_ENGINE')

def find_Web(query, qt=5):
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
    print(response)
    if response.status_code == 200:
        try:
            dados = response.json()
            for item in dados.get("items"):
                if item.get("fileFormat") == "image/png":
                    results.append(item.get("link"))
            return results
        except:
            return []

def show_Results(name_Finded):
    urls = find_Web(name_Finded, 10)
    print(urls)
    for link in urls:
        try:
            response = requests.get(link, verify=False)
            # response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img.show()
        except Exception as e:
            # print(f"Erro ao processar imagem: {link}\nMotivo: {e}\n---")
            continue  