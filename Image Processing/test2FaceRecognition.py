# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:36:18 2020

@author: Raj Tagore
"""

import cv2
from makeTableFaceRecognition import mod

vid = cv2.VideoCapture(0)
while (True):
    a, b = vid.read()
    #read function increments automatically
    if (a==False):
        break
    else:
        n=0
        faceDetector = cv2.CascadeClassifier(r"D:\Padhai\AI\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
        detectedFaces = faceDetector.detectMultiScale(b, scaleFactor = 1.46, minNeighbors = 5)
        for k in detectedFaces:
            n=n+1
            cv2.rectangle(b, (k[0], k[1]), (k[0]+k[2], k[1]+k[3]), (0, 255, 0), 2)
            fp = b[k[1]:k[1]+k[2], k[0]:k[0]+k[3]]
            fp = cv2.resize(fp, (80, 80))
            fp = cv2.cvtColor(fp, cv2.COLOR_BGR2GRAY)
            p = mod.predict(fp)
            if (p[0]==1):
                cv2.putText(b, 'Raj', (k[0], k[1]), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
            else:
                cv2.putText(b, 'Maa', (k[0], k[1]), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
        cv2.imshow('video', b)
        c = cv2.waitKey(1)
        if (c == ord('q')):
            break
cv2.destroyAllWindows()
vid.release()