import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Q5Q6GX-7G25589EV6')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('JARVIS : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

greetMe()

speak('I am JARVIS!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except sr.UnknownValueError:
        speak('Sorry Boss! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        if 'open youtube' in query:
            speak('Sure')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query or 'open chrome' in query:
            speak('Sure')
            webbrowser.open('www.google.co.in')

        elif 'whitehat' in query or 'coding class' in query:
            speak('Sure')
            webbrowser.open('https://code.whitehatjr.com/s/dashboard')

        elif 'open gmail' in query:
            speak('Sure')
            webbrowser.open('www.gmail.com')

        elif 'open video editor' in query:
            speak('Sure')
            location = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Wondershare\\Filmora9"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[1]))

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")   

        elif 'open powerpoint' in query:
            speak('Sure')
            location = "C:\\Program Files\\Microsoft Office\\root\\Office16"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[304]))

        elif 'open excel' in query:
            speak('Sure')
            location = "C:\\Program Files\\Microsoft Office\\root\\Office16"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[72]))

        elif 'open opera' in query:
            speak('Sure')
            location = "C:\\Users\\anay\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[12]))

        elif 'open teams' in query:
            speak('Sure')
            location = "C:\\Users\\anay\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[10]))

        elif 'open team' in query or 'school class application' in query :
            speak('Sure')
            location = "C:\\Users\\anay\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[10]))



        elif 'open zoom' in query:
            speak('Sure')
            location = "C:\\Users\\anay\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[0]))
    
        elif 'open word' in query:
            speak('Sure')
            location = "C:\\Program Files\\Microsoft Office\\root\\Office16"
            softwares = os.listdir(location)
            os.startfile(os.path.join(location, softwares[375]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\Users\\Jarvis Artificial Intelligence\\Jarvis.py"
            os.startfile(codePath)

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on " + "Sir" + ", I will show you where " + location + " is.")
            webbrowser.open("https://www.google.com/maps/place/" + location)

        elif "my location" in query or "where am i" in query:
            speak("Just give me a moment. Here")
            webbrowser.open("https://www.google.com/maps/place/Silver+City,+Sector+93,+Noida,+Uttar+Pradesh+201304")

        elif "weather" in query:
            speak("Just give me a moment. Here")
            webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN795IN795&sxsrf=ALeKk01ieILQpfgslZrDt61nZET70mAZQA%3A1596467851473&ei=iyooX7O-HM2a4-EP3s2cyAc&q=weather&oq=weather&gs_lcp=CgZwc3ktYWIQAzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgQIABBHUOkuWOAzYKo3aABwAXgBgAG-AYgB9AOSAQMwLjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjzr7qZqv_qAhVNzTgGHd4mB3kQ4dUDCAw&uact=5&dlnr=1&sei=xCooX5ulGIn_9QOIwpKwBw")

        elif 'write email' in query or 'send email' in query or 'email' in query:
            try:
                speak("Sir please help me with the email id.")
                emailid = input("Enter the email id: ") 
                speak("What should I say?")
                content = myCommand()
                to = emailid    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")    



        elif 'nothing' in query or 'quit' in query or 'stop' in query or 'abort' in query:
            speak('okay')
            speak('Bye Sir, have a nice day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Boss')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif "what is your name" in query or 'your name' in query:
            speak("My name is Jarvis")
                                    
        elif 'play music' in query:
            music_dir = 'D:\\Music Favourites'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Sure. Just a moment")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'search for' in query:
            query = query.split("for ")
            word = query[1:]
            webbrowser.open(f"{word}")

        else:
            query = query
            speak('Searching...')
            try:
                
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
        
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')
        
        speak('Is there anything left?')






