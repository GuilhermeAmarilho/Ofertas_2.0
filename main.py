import time, os
from multiprocessing import Pool, cpu_count
from Cartaz import generate_All_Items, generate_Exemple_Items
start = time.time()


if __name__ == '__main__':
    
    # generate_Exemple_Items(view = True, who = "Paisagem")
    # generate_Exemple_Items()
    generate_All_Items()
    pass


end = time.time()
print("{:.6f} segundos".format(end - start))