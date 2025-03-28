from Config import get_Config
from Cartaz import get_Cartaz
import time

start = time.time()

get_Cartaz("Paisagem", ["BIFE DE", "PRIMEIRA Kg"], "36,99")

end = time.time()
print("Tempo de execução (recursivo): {:.6f} segundos".format(end - start))