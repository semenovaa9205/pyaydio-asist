
from winsound import PlaySound
from gtts import gTTS
import time
import random
import speech_recognition as sr 
from pyaudio import *
def listen_comand():
 r=sr.Recognizer()
 with sr.Microphone() as source:
  print("Cкажите вашу команду:")
  audio=r.listen(source)
  try:
    spich=r.recognize_google(audio,languge="ru_RU")
    print("вы сказали"+spich)
    return spich
  except sr.UnknownValueError:
     print("неизвестнная ошика")
  except sr.RequestError :
      print("ошибка обработки файла")

    
    
    #return input("Cкажите вашу команду:")
def do_this_comand(message):
     message=message.lower()
     if "как тебя зовут?" in message:
         say_message("меня зовут лиза!")
     elif "привет лиза" in message:
         say_message("приветик") 
     elif "пока лиза": 
         say_message("пока солнышко!")
         exit()
     else :
      say_message('команнда не распознана!!')
def say_message(message):
    voice=gTTS(message, lang="ru")
    file_voice_name= "_saundvoice"+str(time.time())+"_"+str(random.randint(0,10000))+"mp3"
    voice.save(file_voice_name)
    PlaySound.playsound(file_voice_name)
    print("Голосовой ассистент"+message)
if __name__=='__main__':
     while True:
      comand=listen_comand()
      do_this_comand(comand)





    
        
     
 
