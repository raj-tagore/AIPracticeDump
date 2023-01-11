# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:38:21 2020

@author: Raj Tagore
"""

import cv2
vid = cv2.VideoCapture('D:\Padhai\AI\FaceRecognitionVideo.mp4')
while (True):
    a, b = vid.read()
    #read function increments automatically
    if (a==False):
        break
    else:
        n=0
        faceDetector = cv2.CascadeClassifier(r"D:\Padhai\AI\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
        detectedFaces = faceDetector.detectMultiScale(b, scaleFactor = 1.46, minNeighbors = 5)
        for i in detectedFaces:
            n=n+1
            cv2.rectangle(b, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (0, 255, 0), 2)
            cv2.putText(b, 'face: '+str(n), (i[0], i[1]), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
        cv2.imshow('video', b)
        b = cv2.waitKey(1)
        if (b == ord('q')):
            break
cv2.destroyAllWindows()
vid.release()