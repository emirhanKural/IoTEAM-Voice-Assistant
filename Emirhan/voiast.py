from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import time

import speech_recognition as sr
import pyttsx3 #yeni speakerımız
import pytz
import subprocess
import cv2 

#gtts.lang.tts_langs() dillerin listesi
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[2].id) 
    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()
    
    
    
def get_audio():
    r = sr.Recognizer()
    
    while True:
        try: 
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""
                said = r.recognize_google(audio,language = "tr-TR") ##google api ile ne söylendiğini anlamlandırıyoruz. "tr-TR"
                print(said)
                break
        except Exception as e:
            print("Emir Bekliyor: ",str(e))
            
    return said.lower()  

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name]) #uygulamaları açmak için subprocess
    
def photo():
    photo = cv2.VideoCapture(0)
    ret, frame = photo.read() 
    cv2.imwrite('frame.jpg', frame) 
    photo.release()

WAKE = "uyan"
STOP = "yeterli"
print("Start")

while True:
    print("Dinliyorum")
    text = get_audio()
    if text.count(STOP) >0:
        speak("Görüşmek üzere efendim")
        break

    if text.count(WAKE) > 0:
        speak("Sizi dinliyorum efendim")
        text = get_audio()
        NOTE_STRS = ["bir not yaz", "not defteri", "bunu hatırla", "yazı yaz","not yaz"]
        for phrase in NOTE_STRS:
            if phrase in text:
                speak("Ne yazmak istersiniz efendim? ")
                note_text = get_audio()
                note(note_text)
                speak("Söylediklerinizi not aldım efendim.")
                break
        
        PHOTO_STRS = ["foto çek","resim çek","resimli"]
        for phrase in PHOTO_STRS:
            if phrase in text:
                speak("Resmi Çekiyorum Efendim")
                photo()
                speak("Resmi Çektim Efendim")
                break