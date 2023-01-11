# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:13:09 2020

@author: Raj Tagore
"""

import pyttsx3
ttsobj = pyttsx3.init('sapi5')
voices = ttsobj.getProperty('voices')
print(voices)
ttsobj.setProperty('voice', voices[0].id)
sentence = input("what to say?\n")
ttsobj.say(sentence)
ttsobj.runAndWait()