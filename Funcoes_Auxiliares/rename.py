import os
import unidecode

def remover_acentos(texto):
    return unidecode.unidecode(texto)

# Mover o arquivo para a pasta necessaria e rodar de la

def renomear_arquivos(raiz="."):
    for dirpath, dirnames, filenames in os.walk(raiz):
        for nome_antigo in filenames:
            nome_novo = remover_acentos(nome_antigo)
            if nome_antigo != nome_novo:
                caminho_antigo = os.path.join(dirpath, nome_antigo)
                caminho_novo = os.path.join(dirpath, nome_novo)

                # Evita sobrescrever arquivos existentes
                if not os.path.exists(caminho_novo):
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {nome_antigo} → {nome_novo}")
                else:
                    print(f"⚠️ Já existe: {nome_novo} — pulando")

if __name__ == "__main__":
    renomear_arquivos(".")  # "." significa a pasta atual (raiz)
