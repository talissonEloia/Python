from selenium import webdriver
from time import sleep

navegador = webdriver.Chrome()
navegador.get("https://producao.ufc.br/pt/documentos/")

clicar = navegador.find_element_by_xpath('/html/body/div[4]/main/article/ul[2]/li[3]')
clicar.click()
sleep(10)
#navegador.find_element_by_xpath('/html/body/div[4]/main/article/ul[2]/li[3]/a')


#navegador.find_element_br_xpath()
