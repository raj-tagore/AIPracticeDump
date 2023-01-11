# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:32:32 2020

@author: Raj Tagore
"""

import cv2
img = cv2.imread(r"D:\Padhai\AI\detectBody.png", 0)
bodyDetector = cv2.CascadeClassifier(r"D:\Padhai\AI\opencv-master\opencv-master\data\haarcascades\haarcascade_fullbody.xml")
detectedBodies = bodyDetector.detectMultiScale(img, scaleFactor = 1.46, minNeighbors = 5)
for i in detectedBodies:
    cv2.rectangle(img, (i[0], i[1]), (i[0]+i[2], i[1]+i[3]), (0, 255, 0), 2)
cv2.imshow("body detector", img)
cv2.waitKey(0)
