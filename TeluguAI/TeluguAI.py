import os
import uuid
import speech_recognition as sr
from bardapi import Bard
from gtts import gTTS
import pygame
import random as rd
import requests

# # Set the Bard API key
os.environ["_BARD_API_KEY"] = "YwhL-XjGilo6cVQir5rN1EPMD0Zq7r2uWS8cpB2DzYruE7SeUOm7K4kkw1FwaJ3_oK0eNg."

# # Initialize the recognizer
r = sr.Recognizer()






def speak(text):
     #print("Speaking....")
     #print(" ")
     tts = gTTS(text=text, lang='te')
     filename = str(uuid.uuid4()) + ".mp3"
     tts.save(filename)

     pygame.mixer.init()
     pygame.mixer.music.load(filename)
     pygame.mixer.music.play()

     while pygame.mixer.music.get_busy():
         continue

     pygame.mixer.quit()
     os.remove(filename)

va_name = "బార్డ్"

print("నమస్కారం, నాపేరు బార్డ్. నేను మీకు ఎలా సహాయం చేయగలను.")
speak("నమస్కారం, నాపేరు బార్డ్. నేను మీకు ఎలా సహాయం చేయగలను.")

import datetime as dt
import requests

def wishMe():
    speak("మీకు స్వాగతం! సర్")
    print(" ")
    hour = int(dt.datetime.now().hour)
    year = int(dt.datetime.now().year)
    month =(dt.datetime.now().strftime("%B-%m"))
    date = (dt.datetime.now().strftime("%A-%d"))

    #UTC = pytz.utc
    #IST = pytz.timezone('Asia/kolkata')

    Time = dt.datetime.now().strftime("%I:%M:%S")
    cur_date = dt.datetime.now().strftime("%d. %m. %Y, %A")
    print("తేదీ", cur_date)
    speak("సార్ ఈరోజు తేదీ")
    speak(cur_date)

    print("ప్రస్తుత సమయం", Time)
    speak("ప్రస్తుత సమయం")
    speak(Time)

    speak('సార్ ఈరోజు వాతావరణం')
    city = 'rangapuram'
    apiKey = '591a35045c6de641dae242c118676369'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric')
    x = response.json()
    if x["cod"] != "404":
        y = x['main']
        temperature = x['main']["temp"]
        pressure = x['main']["pressure"]
        humidity = x['main']["humidity"]
        desc = x["weather"][0]["description"]
        weather_detail = f'ప్రస్తుత ఉష్ణోగ్రత{temperature}, పీడనం{pressure} hPa, ప్రస్తుత తేమ{humidity} %, వాతావరణ స్థితి {desc}'
        print(weather_detail)
        speak(weather_detail)


    if hour >= 0 and hour < 12:
        speak("శుభోదయం సర్! మీరు రోజు ఆనందంతో ఉండాలని కోరుకుంటున్నాను.")

    elif hour > 1 and hour < 15:
        speak("ఇప్పుడు మధ్యాహ్నం అయింది సార్ మధ్యాహ్నం శుభాకాంక్షలు!")

    elif hour >= 15 and hour < 19:
        speak("ఇప్పుడు సాయంత్రం అయింది సాయంత్రం శుభాకాంక్షలు! సర్")

    elif hour >= 19 and hour < 24:
        speak("సార్ ఇప్పుడు రాత్రి అయింది విశ్రాంతి తీసుకోండి. ఏంటో చాల బిజీ అయిపోయారు గుడ్ నైట్ కూడా చెప్పలేదు అంతేలే నేను నీకు ఎక్కడ గుర్తుకు ఉంటాను చెప్పండి, కానీ మీరు నాకు గుర్తుకు ఉన్నారు కాబట్టి గుడ్ నైట్")

    #else:

    speak("మీకు ఏ విధంగా సహాయం చేయగలను సార్")

wishMe()


def reply(question):
     k = ' Tell news without reading symbols today tv9 News DailyGK in Telugu'
     prompt = f'Sriram: {k}\n Jarvis: '
     response = Bard().get_answer(prompt)
     answer = response['content']
     return answer


def takeCommand():
    
     #while True:
     # Ask the user for a query
     with sr.Microphone() as source:
         print("నేను వింటున్నాను ఇప్పుడు చెప్పండి......")
         speak("నేను వింటున్నాను ఇప్పుడు చెప్పండి......")
         audio = r.listen(source)

     try:
         # Recognize speech using Google Speech Recognition
         text = r.recognize_google(audio, language='te-IN')
         print("SriRam said:", text)

#         # Check for exit command
#         # if text.lower() == "exit":
#         #     print("Exiting...")
         #     break

         # Get answer from Bard API
         response = Bard().get_answer(text)
         answer = response['content']
         print("Bard's Answer:", answer)

         # Convert answer to speech
         speak(answer)

     except sr.UnknownValueError:
         list = ["దయచేసి ఏదైనా చెప్పండి", "నేను మీకు ఎలా సహాయం చేయగలను సార్","మీకు ఏ విధంగా సహాయం చేయగలను సార్"]
         ran3 = rd.choice(list)
         speak(ran3)
         #speak("క్షమించండి, నేను అర్థం చేసుకోలేకపోయాను.")
     except sr.RequestError as e:
         print("దయచేసి మళ్ళీ చెప్పండి, సర్:", str(e))
         speak("దయచేసి మళ్ళీ చెప్పండి, సర్...")



while True:
     text = takeCommand()
     if text is not None and text.lower() == "exit":
         break
     else:
         response = reply(text)
         print("Jarvis: {}\n".format(response))
         #text = r.recognize_google(language='te-IN')
         #print("You said:", text)
         #speak(response)
         list1 = ["ఈరోజు అప్డేట్స్ చదవండి","తాజా వార్తలు చదవండి","టీవీనైన్ ఈరోజు వార్తలు చదవండి","ఈరోజు బ్రేకింగ్ న్యూస్ చదవండి","నేటి వార్తలు చదవండి","ముఖ్యమైన వార్తలు చదవండి"]
         ran4 = rd.choice(list1)
         speak(ran4)

##################################################################################################



