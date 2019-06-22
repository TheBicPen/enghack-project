#!/usr/bin/env python

import cv2
import os
from time import sleep
from google.cloud import vision

def classify(image):
    # Imports the Google Cloud client library
    

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    image_types = vision.types.Image(content=image)
    
    
    # Performs label detection on the image file
    response = client.label_detection(image=image_types)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

def detect_logos(path):
    """Detects logos in the file."""
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

if __name__ == '__main__':
    # with io.open("scrot.bmp", 'rb') as image_file:
    #     content = image_file.read()

    stream = cv2.VideoCapture(0)
    successful_frames = 0
    while(True):
        sleep(1) # 1 fps
        ret, frame = stream.read()
        if ret:
            successful_frames += 1    
            classify(str(frame))
            cv2.imshow(frame)
        else:
            print("Dropped a frame! {0} frames succeeded.".format(successful_frames))
            successful_frames = 0
