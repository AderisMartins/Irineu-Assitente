import pygame.mixer
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load(open("mensagem.mp3","rb"))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
print ("done")