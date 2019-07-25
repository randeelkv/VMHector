import  speech_recognition as sr
import pyttsx3
from datetime import datetime

speach = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver is not found.")
except RuntimeError:
    print("Driver fails to initialize.")

#this gets the list of voices to to print
voices = engine.getProperty('voices')
#display the list of voices
for voice in voices:
    print(voice.id)

#set the voice after picking from the program
engine.setProperty( 'voice' , 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK' )
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

# engine.say("Hi Viiraj..., It's Hector..., Your Virtual Assistant..., Nice to See you..")
# engine.runAndWait()

def speak_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print("Listning now ........")
    with sr.Microphone() as source:
        audio = speach.listen(source)
    try:
        voice_text = speach.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Sorry: Network error")
    return voice_text

def read_time():
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    d = date_time.strftime("%I %M%p")
    print("Output 4:", d)
    return d

if  __name__ == '__main__':
    speak_cmd("Hi Veraj..., It's Hector..., Your Virtual Assistant..., Nice to See you..")

    while True:
        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if "hello" in voice_note:
            speak_cmd("Hi Again")
        elif 'run' in voice_note:
            speak_cmd("sorry .. I cannot run")
        elif (('Hector time please' in voice_note) or ('time please' in voice_note )):
            speak_cmd(read_time())
            
        elif 'bye' in voice_note:
            speak_cmd("Bye.. Have a Nice Day ")
            exit()