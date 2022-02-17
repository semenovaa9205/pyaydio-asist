from ast import If
from email import message
import os
import json
from gtts import gTTS
import time
import random
import speech_recognition as sr 

def listen_comand():
 r=sr.Recognizer()
 with sr.Microphone() as source:
  print("Cкажите вашу команду:")
  audio=r.listen(source)
  try:
    spich=r.recognize_google(audio,language="ru-RU")
    print("вы сказали"+spich)
    return spich
  except sr.UnknownValueError:
     print("неизвестнная ошика")
  except sr.RequestError :
      print("ошибка обработки файла")

    
    
    #return input("Cкажите вашу команду:")
def do_this_comand(message):
     message=message.lower()
    
     db={
     "intents":{
          'hello':{
           "examples":["привет","хай"],
           "responses":["приветик","хающки"]

          },

        'poka':{
         
           "examples" :["пока","до встречи"],
           "responses":["пока солнкнышко!","я буду вас ждать хозяин!"]
          },
          'name':{
             "examples":["как тебя зовут?","как твоё имя?","скажи своё имя"],
              "resposes":["меня зовут лиза ","лизанька", "елизавета"]
          }
             } 
             }
     for intent in db["intents"].keys():
      for example in db["intents"][intent]["examples"]:
                      if message==example:
                    return  say_message(random.choice(db["intents"][intent]["responses"]))
                      else:
                       return say_message('команнда не распознана!!')    
                           
                           
   
      
                        
      
            
def   say_message(message):
  voice=gTTS(message, lang="ru")
  file_voice_name="D:\pytich\saundasist\_iisoundvoice_"+str(time.time())+"_"+str(random.randint(0,10000))+".mp3" 
  voice.save(file_voice_name)
  os.startfile(file_voice_name)
  print("Голосовой ассистент"+message)
if __name__=='__main__':
     while True:
      comand=listen_comand()
      do_this_comand(comand)
      





    
        
     
 
