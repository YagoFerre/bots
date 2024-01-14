from selenium import webdriver
import requests

navegador = webdriver.Chrome()
navegador.get('https://www.ioepa.com.br/portal/')
navegador.implicitly_wait(5)

pdf_url = "https://drive.google.com/uc?id=1sFyHAQz4ncuCOOg_pD3jiYlZqIXD1tLx&export=download"

response = requests.get(pdf_url)

with open('../../Downloads/para-diario/para.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)
    print("Download finalizado")


# Extra
pdf_url = "https://drive.google.com/uc?id=1sIqa3bpfApcIGKTGvYGyz2N3mp2LB4D6&export=download"

response = requests.get(pdf_url)

with open('../../Downloads/para-diario/para-extra.pdf', 'wb') as pdf_file:
    pdf_file.write(response.content)
    navegador.quit()
    print("Download finalizado")
