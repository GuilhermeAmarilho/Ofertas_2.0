from Storage.Lista_Promo import getListItems
from Google_Search_API.Search_API import buscar_google
from PIL import Image
from io import BytesIO
import requests

def get_Encarte():
    items = getListItems()
    print('\n\n\n\n\n')
    url = buscar_google("Costela janela kg")[0]
    
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
    # buscar_google("Iphone")
    # for item in items:
    #     print(item)

# Exemplo de uso