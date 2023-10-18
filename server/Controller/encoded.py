import face_recognition
import os
import cv2
import numpy as np

path = os.getcwd()+"/Faces"                   #Add Your url 

classNames = [os.path.splitext(file)[0] for file in os.listdir(path)]

images = [cv2.imread(os.path.join(path, file)) for file in os.listdir(path)]

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if face_recognition.face_encodings(img):
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)