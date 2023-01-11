# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:21:32 2020

@author: Raj Tagore
"""

import cv2
import os
import numpy as np

faceDetector = cv2.CascadeClassifier(r"D:\Padhai\AI\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
        
for i in os.listdir("D:\Padhai\AI\Person1"):
    pic = cv2.imread(r"D:\Padhai\AI\Person1"+"/"+i, 0)
    fd = faceDetector.detectMultiScale(pic, scaleFactor = 1.46, minNeighbors = 5)
    for j in fd:
        fpic = pic[j[1]:j[1]+j[2], j[0]:j[0]+j[3]]
        fpic = cv2.resize(fpic, (80, 80))
        cv2.imwrite(r"D:\Padhai\AI\bw1"+"/"+i, fpic)
        

    
        
'''pic = cv2.imread(r"D:\Padhai\AI\Person1"+"/"+"T1.jpg", 0)
fd = faceDetector.detectMultiScale(pic, scaleFactor = 1.46, minNeighbors = 5)
for i in fd:
    cv2.rectangle(pic, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (0, 255, 0), 2)
    cv2.putText(pic, 'face', (i[0], i[1]), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
    fpic = pic[i[1]:i[1]+i[2], i[0]:i[0]+i[3]]
    fpic = cv2.resize(fpic, (80, 80))
cv2.imshow('pic', fpic)
cv2.waitKey(0)'''

