# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:50:14 2020

@author: Raj Tagore
"""

import datetime
import pyttsx3
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
import os

#tts setup
ttsobj = pyttsx3.init('sapi5')
voices = ttsobj.getProperty('voices')
ttsobj.setProperty('voice', voices[0].id)
#stt setup
r = sr.Recognizer()

start = input("Start?")
if start=='y':
    x = datetime.datetime.now()
    
    if (int(x.strftime('%H'))<12):
        ttsobj.say("Good morning, select one of the options")
        ttsobj.runAndWait()
    else:
        ttsobj.say("Good evening, select one of the options")
        ttsobj.runAndWait()
    print("\n1: send an email\n")
    c = int(input())
    while (c==1):
        ttsobj.say("speak the subject for your email:")
        ttsobj.runAndWait()
        with sr.Microphone() as ears:
            print("speak: ")
            r.pausethreshold = 1
            r.adjust_for_ambient_noise(ears, duration=1)
            audiostring = r.listen(ears)
        try:
            subject = r.recognize_google(audiostring).lower()
            print('Your subject is: ' + subject + '\n')
            print('sending...')
            #msg = MIMEText(subject)
            email={}
            email['Subject'] = subject
            email['From'] = 'usernamerajtagore@gmail.com'
            email['To'] = 'usernamerajtagore@gmail.com'
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.connect("smtp.gmail.com",587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('usernamerajtagore@gmail.com', 'T.raj0708/')
            s.sendmail('usernamerajtagore@gmail.com', 'usernamerajtagore@gmail.com', subject)
            s.quit()
        except sr.UnknownValueError:
            print('couldnt understand please speak again')
            continue
        
    
