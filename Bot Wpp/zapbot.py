from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


class WhatsappBot:
    def __init__(self): #define iniciação do codigo
        self.mensagem = "Hello Word - Bot Teste" #menssagem enviada
        self.grupos = ["Confraria del Negron 2.0"] #Nome do grupo, necessita ser igual ao nome real
        options = webdriver.ChromeOptions() #cria objeto tipo webdrive
        options.add_argument('lang=pt-br') #define o idioma
        self.drive = webdriver.Chrome(ChromeDriverManager().install(), options = options) #local do webdrive

    def EnviarMenssagens(self):
        self.dev.get('https://web.whatsapp.com')
        time.sleep(30)
        def waiting():
            try:
                self.driver.find_element_by_xpath("//canvas[@aria-label='Scan me!']")
            except: return False
            else: return True
        while(waiting() == True):
           print('Leia o codigo QR!')
        print('OK')

        for grupo in self.grupos:
            grupo = self.drive.find_element_by_xpath(f"//span[@title={grupo}]")
            time.sleep(3)

            grupo.click()
            chat_bot = self.drive.find_element_by_class_name("_3Uu1_")
            time.sleep(3)

            chat_bot.click()
            chat_bot.send_keys(self.mensagem)
            botao_enviar = self.drive.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)

            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMenssagens()