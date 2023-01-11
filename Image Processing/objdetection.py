# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:17:08 2020

@author: Raj Tagore
"""

from imageai.Detection import ObjectDetection
#import os

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
custom = detector.CustomObjects(person=True, umbrella=True)
detections = detector.detectCustomObjectsFromImage( custom_objects=custom, input_image='objrecog.jpg', output_image_path='simg2.jpg', minimum_percentage_probability=32)
for obj in detections:
    print(obj["name"])

