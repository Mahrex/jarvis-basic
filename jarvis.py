# using for text-to-speech communication
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import os
import time

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
        print(f"User said: {query}\n")
    except Exception as e:
        print('Please say that again...!')
        return 'None'
    
    return query # what the user said is being returned
    
if __name__ == '__main__':
    wishMe()
    
    # tasks that can Jarvis do for us
    awake = True 
    while awake:
        query = take_command().lower() # storing the data, user is saying
        
        # searching for something, someone 
        if 'wikipedia' in query or 'do you know' in query or 'who is' in query:
            speak('Searching...')
            results = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia...')
            print(results)
            speak(results)
        
        # opening websites in webbrowser    
        elif 'open google' in query: # done
            print('Opening google')
            speak('Opening google sir')
            webbrowser.open('https://www.google.com/')
             
        elif 'open youtube' in query: # done
            print('Opening youtube')
            speak('Opening youtube sir')
            webbrowser.open('https://www.youtube.com/')
            
        elif 'open github' in query: # done
            print('Opening github')
            speak('Opening github sir')
            webbrowser.open('https://github.com/')
            
        elif 'open linkedin' in query: # done
            print('Opening linkedin')
            speak('Opening linkedin sir')
            webbrowser.open('https://www.linkedin.com/feed/')
            
        elif 'open outlook' in query: # done 
            print('Opening outlook')
            speak('Opening outlook sir')
            webbrowser.open('https://outlook.live.com/mail/0/')
            
        elif 'open email' in query: # done
            print('Opening email')
            speak('Opening email sir')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            
        elif 'open facebook' in query: # done
            print('Opening facebook')
            speak('Opening facebook sir')
            webbrowser.open('https://www.facebook.com/')
            
        elif 'open twitter' in query: # done
            print('Opening twitter')
            speak('Opening twitter sir')
            webbrowser.open('https://twitter.com/home')
            
        elif 'open whatsapp' in query: # done
            print('Opening whatsapp')
            speak('Opening whatsapp sir')
            webbrowser.open('https://web.whatsapp.com/')
        
        elif 'open stack overflow' in query: # done
            print('Opening stackoverflow')
            speak('Opening stackoverflow')
            webbrowser.open('https://stackoverflow.com/')
            
        # get the current time
        elif 'the time' in query: # done
            str_time = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'Time is {str_time}')
            speak(f'Sir the current time is {str_time}')
            
        # get the date
        elif 'the date' in query: # done
            str_date = datetime.datetime.now().strftime('%d/%m/%y')
            print(f'Date is {str_date}')
            speak(f'Sir the current date is {str_date}')
        
        # clear output screen
        elif 'clear screen' in query: # done
            speak('Clearing screen sir.')
            os.system('cls')
            
        # open apps and softwares
        elif 'open code' in query: # done
            code_path = "C:\\Users\\shaun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print('Opening VS Code')
            speak('Opening VS code sir')
            os.startfile(code_path)
            
        elif 'open server' in query: # fix
            server_path = ' "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe" "--defaults-file=C:\\ProgramData\\MySQL\\MySQL Server 8.0\\my.ini" "-uroot" "-p" '
            print('Opening MySQL Server')
            speak('Opening MySQL Server sir')
            os.startfile(server_path)
            
            
        # switch off jarvis
        elif 'switch off' in query:
            print('Switching off...!')
            speak('Going to sleep sir.')
            awake = False