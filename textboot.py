import sys

def listen_comand():
    
    
    return input("Cкажите вашу команду:")
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
    print(message)
if __name__=='__main__':
     while True:
      comand=listen_comand()
      do_this_comand(comand)





    
        
     
 
