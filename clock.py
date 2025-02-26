
from datetime import datetime
import time
def definir_Hora_Atual():
    return datetime.now()
def pegar_Milissegundos(tempo):
    return tempo.microseconds // 1000
def pegar_Segundos(tempo):
    return tempo.seconds % 60 
def pegar_Minutos(tempo):
    return (tempo.seconds % 3600) // 60
def pegar_Horas(tempo):
    return tempo.seconds // 3600
def retornar_Tempo_Gasto(tempo_Inicial):
    tempo_Final = datetime.now() - tempo_Inicial
    string = "tempo decorrido:"
    if pegar_Horas(tempo_Final) != 0:
        string += ' ' + str(pegar_Horas(tempo_Final)) +'h'
    if pegar_Minutos(tempo_Final) != 0:
        string += ' ' + str(pegar_Minutos(tempo_Final)) +'m'
    if pegar_Segundos(tempo_Final) != 0:
        string += ' ' + str(pegar_Segundos(tempo_Final)) +'s'
    if pegar_Milissegundos(tempo_Final) != 0:
        string += ' ' + str(pegar_Milissegundos(tempo_Final)) +'ms'
    return string