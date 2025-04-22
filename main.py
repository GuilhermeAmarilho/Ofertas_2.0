from Cartaz import generate_All_Items, generate_Exemple_Items
from Data import getListItems
import time, os
from multiprocessing import Pool, cpu_count

start = time.time()


if __name__ == '__main__':
    

    # rodou em 15seg
    # i = 0
    # for item in getListItems():
    #     i += 1
    #     get_Cartaz("Retrato", item[0], item[2]).save(cartaz_List_Path+"Retrato "+str(i)+".png")
    #     get_Cartaz("Paisagem", item[1], item[2]).save(cartaz_List_Path+"Paisagem "+str(i)+".png")
    # generate_All_Items()
    # generate_Exemple_Items(view = True, who = "Paisagem")
    generate_Exemple_Items()



end = time.time()
print("{:.6f} segundos".format(end - start))