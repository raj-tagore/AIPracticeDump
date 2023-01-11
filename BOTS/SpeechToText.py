# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:22:02 2020

@author: Raj Tagore
"""

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as ears:
    print("speak: ")
    r.pausethreshold = 1
    r.adjust_for_ambient_noise(ears, duration=1)
    audiostring = r.listen(ears)
try:
    command = r.recognize_google(audiostring).lower()
    print('You said:' + command + '\n')
except sr.UnknownValueError:
    print('.....')
'''def myCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('say something..')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audiostring = r.listen(source)
    try:
        command = r.recognize_google(audiostring).lower()
        print('You said:' + command + '\n')
    except sr.UnknownValueError:
        print('.....')
myCommand()'''
    