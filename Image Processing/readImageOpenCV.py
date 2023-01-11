# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:21:41 2020

@author: Raj Tagore
"""

import cv2
a = cv2.imread(r"C:\Users\Raj Tagore\Pictures\Screenshots\Screenshot (1).png", 0)
cv2.imshow("lol", a)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite(r"D:\Padhai\AI\OpenCVfirstimg2.jpg", a)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()