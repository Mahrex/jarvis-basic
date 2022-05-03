# using for text-to-speech communication
import pyttsx3
import pyaudio

# will take commands
import speech_recognition as sr

import datetime

# setting up our voice to speech
engine = pyttsx3.init('sapi5') # to get the voices from microsoft

voices = engine.getProperty('voices') # get the voice properties
engine.setProperty('voice',voices[0].id) # declaring our Jarvis's voice

# declaring the speak method
def speak(audio):
    '''This will speak the audio that is be passed as an argument'''
    
    engine.say(audio)
    engine.runAndWait()
    
# define the wish me method, Jarvis will wish us on basis of current time
def wishMe():
    '''Jarvis will wish us on basis of current time'''
    
    current_time = int(datetime.datetime.now().hour)
    if current_time >= 0 and current_time <= 12:
        speak('Good morning sir!')
    elif current_time > 12 and current_time <= 18:
        speak('Good afternoon sir!')
    else:
        speak('Good evening sir!')
    
    speak('I am Jarvis, how can I help you?')
    
# taking commands as an input
def take_command():
    '''This will take mic commands from the user and will return the outputs'''
    
    # creating the recognizer instance
    r = sr.Recognizer()
    
    # using the mic as named 'source' getting what the user is saying
    mics = sr.Microphone.list_microphone_names()
    with sr.Microphone() as source:
        print('Listening...!')
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
       
    # handling possible errors
    try:
        print('Recognizing...!') # recognizing the audio that user said
        query = r.recognize_google(audio, language='en-in') # get the data in Indian accent
        print(f"User said : {query}\n")
    except Exception as e:
        print('Please say that again...!')
        return 'None'
    
    return query # what the user said is being returned
    
if __name__ == '__main__':
    wishMe()
    take_command()