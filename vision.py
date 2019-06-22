#!/usr/bin/env python
import io

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
    
    with io.open("/home/alex/Pictures/backgrounds/glowing_lake.jpg", 'rb') as image_file:
        content = image_file.read()

    classify(content)
