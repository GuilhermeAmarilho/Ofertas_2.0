# import time, os
# from multiprocessing import Pool, cpu_count
# from Cartaz import generate_All_Items, generate_Exemple_Items
# start = time.time()
# if __name__ == '__main__':
#         # generate_Exemple_Items(view = True, who = "Paisagem")
#     # generate_Exemple_Items()
#     generate_All_Items()
# end = time.time()
# print("{:.6f} segundos".format(end - start))

# from Web.Start_Flask import app
import os
from PIL import Image
from io import BytesIO
import requests


os.system('cls')
from Image_Location.Find_In_Files import Find_File
from Image_Location.Find_In_Web import find_Web

# print(find_Web("Maça nacional"))
def get_Encarte(name_Find):
    urls = find_Web(name_Find, 10)
    print(urls)
    for link in urls:
        try:
            response = requests.get(link, verify=False)
            response.raise_for_status()  # Garante que códigos HTTP de erro sejam tratados
            img = Image.open(BytesIO(response.content))
            img.show()
        except Exception as e:
            print(f"Erro ao processar imagem: {link}\nMotivo: {e}\n---")
            continue  # Só para deixar claro que vai pro próximo

print(Find_File("maça verde"))
get_Encarte("Maçã verde")
    
# if __name__ == '__main__':
    # aqui roda o servidor
    # app.run(host='0.0.0.0', port=8221, debug=True)