from selenium import webdriver
from selenium.webdriver.common.by import By
import time, requests, os
from urllib.parse import quote_plus

def google_images_scrape(query, max_links=4):
    if not "png" in query:
        query = query + " png"
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3") 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 ...")
    # Desativar  o headless se quiser ver o selenium rodando | debugar
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    results = []
    try:
        termo = quote_plus(query)
        url = f"https://www.google.com/search?tbm=isch&q={termo}"
        time.sleep(1)
        driver.get(url)
        time.sleep(3)
        # Talvez tenha que mudar com o tempo, pois pode alterar a class css do item
        sugestoes = driver.find_elements(By.CSS_SELECTOR, ".RntSmf > tbody > tr > td > a > div > img")
        for i in range(0, min(len(sugestoes), max_links * 2), 2):
            link = sugestoes[i].get_attribute("src")
            results.append(link)
    finally:
            driver.quit()
    return results

def baixar_imagens(lista_de_links, destino="imagens", prefixo="img"):
    os.makedirs(destino, exist_ok=True)
    for i, url in enumerate(lista_de_links, start=1):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                caminho = os.path.join(destino, f"{prefixo}_{i}.png")
                with open(caminho, "wb") as f:
                    f.write(response.content)
                print(f"[{i}] OK: {caminho}")
            else:
                print(f"[{i}] Falha ({response.status_code})")
        except Exception as e:
            print(f"[{i}] Erro: {e}")
