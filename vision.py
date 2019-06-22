#!/usr/bin/env python
import io
import cv2
from time import sleep

def classify(image):
    # Imports the Google Cloud client library
    from google.cloud import vision

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    image_types = vision.types.Image(content=image)
    
    
    # Performs label detection on the image file
    response = client.label_detection(image=image_types)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

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
            classify(frame)
        else:
            print("Dropped a frame! {0} frames succeeded.".format(successful_frames))
            successful_frames = 0
