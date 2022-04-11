from vosk import Model
import os
import speech_recognition as sr
import pyttsx3 as tts
import core
import json
import pyaudio
from nlu.classifier import classify


speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('rate', 180)
#speaker.setProperty('voice', voices[1].id) English voice


# obtain audio from the microphone
r = sr.Recognizer()
r.non_speaking_duration = 0.1
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    speaker.say("Olá Senhor! Como posso ajudar?")
    speaker.runAndWait()
    audio = r.listen(source)


#Usando API do google para entender oque eu foi dito
try:
    r.recognize_google(audio, language="PT-BR")
except sr.UnknownValueError:
    speaker.say("Desculpe, não entendi, poderia repetir?")
    speaker.runAndWait()
except sr.RequestError as e:
    speaker.say("Você está sem internet no momento, tente novamente mais tarde")
    speaker.runAndWait()

print(r.recognize_google(audio, language="PT-BR").lower())
entity = classify(r.recognize_google(audio, language="PT-BR"))
if entity.lower() == 'time\gettime':
    print(123)







