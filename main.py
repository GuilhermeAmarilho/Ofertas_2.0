from Config import get_Config
from Cartaz import get_Cartaz
import time

start = time.time()

if __name__ == '__main__':
    # cartaz_Type = "Exemplo"  # ou o identificador apropriado
    # textos = ["TEXTO SUPERIOR", "TEXTO DO MEIO", "TEXTO INFERIOR"]
    # cartaz = get_Cartaz(cartaz_Type, textos)
    # get_Cartaz("Paisagem", ["BIFE DE", "PRIMEIRA Kg"], "36,99")
    get_Cartaz("Retrato", ["BIFE DE", "PRIMEIRA" , "Kg"], "36,99")

end = time.time()
print("{:.6f} segundos".format(end - start))