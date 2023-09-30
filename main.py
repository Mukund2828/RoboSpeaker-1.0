import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

print('Welcome to Robospeaker 1.0 created by Mukund')
while(True):
    x = input('Enter what to speak : ')
    if(x=='q'):
        speak.Speak('Thanks,  Exiting')
        break
    else:
        speak.Speak(x)


