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
import os
from Web.Start_Flask import app
os.system('cls')
if __name__ == '__main__':
    # aqui roda o servidor
    app.run(host='0.0.0.0', port=8221, debug=True)