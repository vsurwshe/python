import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio


engine = pyttsx3.init('dummy') 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good eveing sir")

    speak("I am Jarvis sir. How May Help You")    

def takeCommand():
    r=sr.Recognizer()
    print(sr.Microphone().list_microphone_names())
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said :{query}\n")

    except Exception as e:
        print(e)
        print("Say That Again Please.....")
        return "None"
    
    return query


def get_query():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print(r.recognize_google(audio))
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        tts_result = r.recognize_google(audio)
        print('Got ' + tts_result)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    return tts_result 



if __name__=="__main__":
    wishMe()
    takeCommand()
