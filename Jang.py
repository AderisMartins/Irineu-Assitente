from gtts import gTTS
import os.path
import pygame.mixer
from time import sleep
import playsound
import speech_recognition as sr
from requests import get
from bs4 import BeautifulSoup

#####Configurações#####
hotword = 'google'

with open('Python-Assitente-credenciais.json') as credenciais_google:
    credenciais_google = credenciais_google.read()

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando comando!")
            audio = microfone.listen(source)
            try:
                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('comando: ',trigger)
                    responde('Um momento')
                    executa_comandos(trigger)
                    break
            except sr.UnknownValueError:
                print("Eu não entendi! Repita por favor.")
            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
    return trigger

def responde(arquivo_reposta):
    playsound('./audios/'+ arquivo_reposta +'.mp3')

def cria_audio(mensagem):
    for i in range(len(mensagem)):
        tts = gTTS(text=mensagem[i], lang='pt-br')
        file1 = str(str(mensagem[i]) + ".mp3")
        tts.save("noticias_agora/"+file1)

        #####Inicia reprodução de notícias#####
        pygame.mixer.init()
        pygame.mixer.music.load(open('noticias_agora/'+file1, "rb"))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            sleep(1)
        print("done")

#####Verifica o comando chamado#####
def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()

#######Comando de busca por notícias#######
def ultimas_noticias():
    site = get('https://news.google.com/rss?g&gl%27&hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    noticias = noticias.findAll('title')[:4]
    noticias_list = []
    for b in noticias[1:]:
        result = b.text.strip()
        noticias_list.append(result)
    cria_audio(noticias_list)

def main():
    while True:
        monitora_audio()

main()
ultimas_noticias()