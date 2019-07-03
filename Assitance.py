import  speech_recognition as sr
import pyttsx3

try:
    engine = pyttsx3.init()
except ImportError:
    print("error 1")
except RuntimeError:
    print("error 2")

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)

engine.setProperty( 'voice' , 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK' )
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

engine.say("Hi ..., It's Hector..., Your Virtual Assistant..., Nice to See you..")
engine.runAndWait()