from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

navegador = webdriver.Chrome()

navegador.get('https://www.diariooficial.ma.gov.br/')

navegador.implicitly_wait(5)

navegador.find_element(By.XPATH, '//*[@id="clients"]/div/div/div[1]/div/div[8]/div').click()

wait = WebDriverWait(navegador, 10)
download_pdf_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="downloadPDF"]')))
download_pdf_button.click()

pdf_url = "https://www.diariooficial.ma.gov.br/download.php?arqv=1&arq=TE20240112"

# Make a request with appropriate headers and cookies
response = requests.get(pdf_url)

# Save the PDF content to a file
with open('../../Downloads/maranhao-diario/maranhao.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)
    navegador.quit()
    print("Download finalizado")

