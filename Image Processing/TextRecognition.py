# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:21:37 2020

@author: Raj Tagore
"""

import cv2
import pytesseract as pt
from spellchecker import SpellChecker

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
spell = SpellChecker()
img = cv2.imread("TextRecognize/WhatsApp Image 2020-08-08 at 15.28.52 (1).jpeg")
text = pt.image_to_string(img)
print(text)
edited_text = ''
for i in spell.split_words(text):
    spell.correction(i)
    edited_text = edited_text + i + ' '
    
print(edited_text)