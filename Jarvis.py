import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnKnownValueError:
            print(" Not Understand ")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',140)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':


    # if  "hey jarvis" in sptext().lower():
            while True:
                    data1=sptext().lower()

                    if "hello" in data1:
                        question = "good to listen"
                        print(question)
                        speechtx(question)

                    if "your name" in data1:
                        name = "my name is jarvis"
                        print(name)
                        speechtx(name)

                    elif "your creator" in data1:
                        creator = "My creator is Muhammad Absaar"
                        print(creator)
                        speechtx(creator)

                    elif "kya hua" in data1:
                        question = "Kuch Nahi"
                        print(question)
                        speechtx(question)

                    elif 'time' in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        print(time)
                        speechtx(time)

                    elif 'youtube' in data1:
                        webbrowser.open("https://www.youtube.com/")

                    elif 'kali linux' in data1:
                        webbrowser.open("")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en",category="neutral")
                        print(joke_1)
                        speechtx(joke_1)

                        # elif "play song" in data1:
                        #      add = "D:\New folder"
                        #      listsong = os.listdir(add)
                        #      print(listsong)
                        #      os.startfile(os.path.join(add,list[0]))

                    elif "by jarvis" in data1:
                        speechtx("thankyou")
                        break

                    # time.sleep(5)
else:
     print("thanks")