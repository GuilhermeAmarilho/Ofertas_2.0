from Storage.Lista_Promo import getListItems
from Google_Search_API.Search_API import searchIMG
from PIL import Image
from io import BytesIO
import requests

def get_Encarte():
    items = getListItems()
    urls = searchIMG("tico e teco", 10)
    print(urls)
    for link in urls:
        # try:
        response = requests.get(link)
        img = Image.open(BytesIO(response.content))
        img.show()
        # except:
        #     pass