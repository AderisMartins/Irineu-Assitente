from gtts import gTTS
from playsound import playsound as play
def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('./audios/Um momento.mp3')

    #open('./audios/bem_vindo.mp3')
    play('./audios/Um momento.mp3')

cria_audio('Um momento')
