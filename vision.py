#!/usr/bin/env python

import cv2
import io
import os
from time import sleep
from google.cloud import vision

def classify(image, client):
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

def detect_logos(image, client):
    """Detects logos in the file."""
    
    image = vision.types.Image(content=image)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

def get_client():
    return vision.ImageAnnotatorClient()

def get_file(path):
    """
    gets the content of an image
    """
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    return content


if __name__ == '__main__':
    detection = ""
    source = ""
    while source not in list(range(2)):
        source = int(input("Select operation mode:\n0: webcam capture\n1: file\n"))
        # print(source, type(source))
    while detection not in list(range(2)):
        detection = int(input("Select what to detect:\n0: any objects\n1: logos\n"))
    if source == 0:
        stream = cv2.VideoCapture(0)
        successful_frames = 0
        # while(True):
        #     sleep(1) # 1 fps
        ret, frame = stream.read()
        if ret:
            img = cv2.imencode("jpg", frame)
            cv2.imshow("Video Frame", frame)
            cv2.waitKey(2000)
            # successful_frames += 1    
            if detection == 0:
                classify(img, get_client())
            elif detection == 1:
                detect_logos(img, get_client())
        else:
            print("Dropped a frame! {0} frames succeeded.".format(successful_frames))
            successful_frames = 0
    elif source == 1:
        path = input("input a path to an image:\n")
        img = get_file(path)
        if detection == 0:
                classify(img, get_client())
        elif detection == 1:
            detect_logos(img, get_client())