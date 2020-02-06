# impore Open CV Library as CV2
import cv2
#Classifier or Face Detection Model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Reading  input image
img = cv2.imread('MyPic1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y , w ,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 150 , 150), 3)
    # Display the output
cv2.imshow('Detcted Image', img)
cv2.waitKey()