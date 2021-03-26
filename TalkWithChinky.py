import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'chinky' in command:
                command = command.replace('chinky', '')
                print(command)
    except:
        pass
    return command


def run_chinky():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('No I am in a relationship with my best friend')
    elif 'are siri and alexa better than you' in command:
        talk('i like all ais')
    elif 'you are stupid' in command:
        talk('thats not very nice to say')
    elif 'do you work for cia' in command:
        talk('i work for this pc')
    elif 'do you want to go on a date' in command:
        talk('i like you but as a friend')
    elif 'is there a santa' in command:
        talk('i dont know him personaly but i heard a lot of things about santa if i ever meet him i will tell you')
    elif 'what is love' in command:
        talk('romance is the expressive and pleasurable feeling from an emotion toward another person')
    elif 'who was in the kitchen' in command:
        talk('Rashi sister will be there but I will not be able to tell you why she took the gram out of the cooker and put it on the gas of the empty cooker.')
    elif 'what is covid-19' in command:
        talk('coronavirus disease is an infectious disease caused by newly discovered coronavirus and its most common symptoms are fever, dry cough, tiredness')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    else:
        print('please say the command again.')


while True:
    run_chinky()