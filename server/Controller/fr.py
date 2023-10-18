# import cv2
# import face_recognition
# import numpy as np
# from encoded import encoded_face_train,classNames

# cap  = cv2.VideoCapture(1)      # Adjust 0 or 1 according to your camera input
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1024)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,768)
# flag = 0
# ans=[]
# index = 0

# while True:
#     index += 1
#     if(index == 500):       #Change according to your need
#         break
#     success, img = cap.read()
#     imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
#     imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#     faces_in_frame = face_recognition.face_locations(imgS)
#     encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
#     for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
#         matches = face_recognition.compare_faces(encoded_face_train, encode_face)
#         faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
#         matchIndex = np.argmin(faceDist)
#         if matches[matchIndex]:
#             # print(classNames[matchIndex])
#             ans.append(classNames[matchIndex])
#             flag+=1
#             break
#     # cv2.imshow('webcam', img)
#     if (cv2.waitKey(1) & 0xFF == ord('q')) or flag==10:
# #         cap.release()
# #         cv2.destroyAllWindows()
#         print(max(set(ans), key = ans.count))
#         break
# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt % matplotlib inline


# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('../DATA / haarcascades / haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../DATA / haarcascades / haarcascade_eye.xml')



# create a function to detect face
def adjusted_detect_face(img):
	
	face_img = img.copy()
	
	face_rect = face_cascade.detectMultiScale(face_img, 
											scaleFactor = 1.2, 
											minNeighbors = 5)
	
	for (x, y, w, h) in face_rect:
		cv2.rectangle(face_img, (x, y), 
					(x + w, y + h), (255, 255, 255), 10)\
		
	return face_img


# create a function to detect eyes
def detect_eyes(img):
	
	eye_img = img.copy() 
	eye_rect = eye_cascade.detectMultiScale(eye_img, 
											scaleFactor = 1.2, 
											minNeighbors = 5) 
	for (x, y, w, h) in eye_rect:
		cv2.rectangle(eye_img, (x, y), 
					(x + w, y + h), (255, 255, 255), 10)	 
	return eye_img

# Reading in the image and creating copies
img = cv2.imread('../deeps.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

# Detecting the face 
face = adjusted_detect_face(img_copy)
plt.imshow(face)
# Saving the image
cv2.imwrite('face.jpg', face)
