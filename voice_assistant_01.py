import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import time

## SET THE ENGINE
engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

## Hello AI
engine.say('Hello. I\'m your new personal assistant. Marco created me. Let\'s get started! How do you want me to call you?')
engine.runAndWait()
## DEFINE YOUR NAME
with microphone as source:
    print('Listening...')
    mic = recognizer.listen(source)
    my_name = recognizer.recognize_google(mic, language='en-GB')
    engine.say('Ok, I\'ll call you {}'.format(my_name))
    engine.runAndWait()

## DEFINE FEW FUNCTIONS TO INTERACT WITH THE AI
def AI_speak(AI_speech):
    '''
    AI_speak function.
    Translate the speech argument from text into speech
    '''
    global my_name
    engine.say(AI_speech)
    engine.runAndWait()

def user_speak():
    '''
    AI_voiceRecognizer function.
    AI recognizes and understands human language.
    We need a microphone to speak.
    '''
    global my_name
    with microphone as source:  # source object needed
        print('Listening to you {}. . .'.format(my_name))
        mic = recognizer.listen(source)
        # let us to be sure the AI understands us
        try:
            human_voice = recognizer.recognize_google(mic, language='en-GB')    # all possible languages https://cloud.google.com/speech-to-text/docs/languages
            
        except Exception:
            AI_speak('I\'m sorry, I didn\'t get it. Say it again.')

        return human_voice

## WELCOME MESSAGE
AI_speak('Well done {}'.format(my_name))

## WHILE TRUE...
while True:
    AI_speak('What are we gonna do?')
    user = user_speak().lower()
    if 'stack' in user or 'overflow' in user:
        stack_open = webbrowser.open_new_tab('https://stackoverflow.com/')
        AI_speak('Let\'s solve some code, {}'.format(my_name))
        time.sleep(6)

    elif 'youtube' in user:
        AI_speak('What are you looking for in Youtube?')
        yt_search = user_speak()
        AI_speak('Ok. Let\'s search for {}.'.format(yt_search))
        yt_open = webbrowser.open_new_tab('https://www.youtube.com/results?search_query={}'.format(yt_search))
        time.sleep(6)

    elif 'from' in user or 'creator' in user or 'info' in user:
        AI_speak('Marco is my creator. You can find him here...')
        marcoGit_open = webbrowser.open_new_tab('https://github.com/marco-create')
        time.sleep(5)

    break