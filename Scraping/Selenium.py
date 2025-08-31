from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def google_images_scrape(query, max_links=5):
    options = webdriver.ChromeOptions()
    # NÃO usamos headless -> vai abrir a janela do Chrome
    driver = webdriver.Chrome(options=options)

    # Abre o Google Imagens
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    driver.get(search_url)

    time.sleep(3)  # tempo para carregar

    # Pega a primeira miniatura
    thumbnails = driver.find_elements(By.CLASS_NAME, "YQ4gaf")
    print(f"Miniaturas encontradas: {len(thumbnails)}")

    # Mantém o navegador aberto por 10 segundos para você ver
    time.sleep(10)

    driver.quit()
