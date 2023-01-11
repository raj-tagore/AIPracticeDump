# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:42:39 2020

@author: Raj Tagore
"""

import os
import cv2
import numpy as np

pics = []
persons = []

for i in os.listdir(r"D:\Padhai\AI\bw1"):
    pic = cv2.imread(r"D:\Padhai\AI\bw1"+"/"+i, 0)
    pics.append(pic)
    persons.append(1)
    
for j in os.listdir(r"D:\Padhai\AI\bw2"):
    pic = cv2.imread(r"D:\Padhai\AI\bw2"+"/"+j, 0)
    pics.append(pic)
    persons.append(2)
    
persons = np.array(persons)

mod = cv2.face.LBPHFaceRecognizer_create()
mod.train(pics, persons)