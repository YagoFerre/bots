from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Poder Executivo
navegador = webdriver.Chrome()

navegador.get('https://www.cepe.com.br/')

navegador.implicitly_wait(5)

navegador.find_element(By.XPATH, '//*[@id="cookieConsentContainer"]/div[2]/a').click()

navegador.find_element(By.XPATH, '//*[@id="container"]/div[3]/div[3]/div[1]/p[1]/a').click()

wait = WebDriverWait(navegador, 10)
download_pdf_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cadernos-front"]/div/div[2]/div[1]/a')))
download_pdf_button.click()

pdf_url = "https://cepebr-prod.s3.amazonaws.com/1/cadernos/2024/20240113/1-PoderExecutivo/PoderExecutivo(20240113).pdf"

response = requests.get(pdf_url)

with open('../../Downloads/pernambuco-diario/pernambuco-executivo.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)
    print("Download finalizado")


# Poder Legislativo
wait = WebDriverWait(navegador, 10)
download_pdf_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cadernos-front"]/div/div[2]/div[2]/a')))
download_pdf_button.click()

pdf_url = "https://cepebr-prod.s3.amazonaws.com/1/cadernos/2024/20240113/6-PoderLegislativo/PoderLegislativo(20240113).pdf"

response = requests.get(pdf_url)

with open('../../Downloads/pernambuco-diario/pernambuco-legislativo.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)
    navegador.quit()
    print("Download finalizado")
