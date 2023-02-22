import pyautogui    
from time import sleep

# - Passos manuais
# 1 - Clicar e digitar usuario
pyautogui.click(824,451,duration=0.1)
pyautogui.write('talisson')

# 2 - Clicar e digitar senha
pyautogui.click(821,479,duration=0.1)
pyautogui.write('qwe123')

# 3 - Clicar em Entrar
pyautogui.click(717,507,duration=1)

# 4 - Estra⁬ cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        pyautogui.click(586,440,duration = 0.1)
        pyautogui.write(produto)

        quantidade = linha.split(',')[1]
        pyautogui.click(563,467,duration = 0.1)
        pyautogui.write(quantidade)

        preco = linha.split(',')[2]
        pyautogui.click(546,490,duration = 0.1)        
        pyautogui.write(preco)

        pyautogui.click(432,645,duration = 0.1)



# 	4.1 Clicar e digitar produto
# 	4.2 Clicar e digitar quantidade
# 	4.3 ClicAR e digitar preço
# 	4.4 Clicar em 'Registrar"

 