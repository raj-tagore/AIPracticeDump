# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:58:51 2020

@author: Raj Tagore
"""

import cv2

vid = cv2.VideoCapture(0)
n=0
while(True):
    a, b = vid.read()
    if a==False:
        break
    else:
        n=n+1
        cv2.putText(b, str(n), (40, 40), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
        cv2.imshow('TestDataInput', b)
        cv2.imwrite(r"D:\Padhai\AI\Person2\T"+str(n)+".jpg", b)
        b = cv2.waitKey(1)
        if (b == ord('q')):
            break
cv2.destroyAllWindows()
vid.release()
        