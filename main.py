import cv2
import os
import pickle
import numpy as np
import face_recognition
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

img_background = cv2.imread('resources/background.png')

# Importing mode images
folderModePath = 'resources/Modes'
mode_path = os.listdir(folderModePath)
imgModeList = []

for path in mode_path:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding files
print("Loading Encode File....")

file = open("EncodeFile.p", "rb")
encodeListWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListWithIds

print("Encode file Loaded....")
#print(studentIds)
#print(len(imgModeList))

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)

    img_background[162:162+480, 55:55+640] = img
    img_background[44:44 + 633, 808:808 + 414] = imgModeList[3]

    # Compare the encoding and Current Face
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("Matches : ", matches)
        print("faceDistance : ", faceDistance)

        matchIndex = np.argmin(faceDistance)
        print("Match Index", matchIndex)

        if matches[matchIndex]:
            #print("Known Face Detected.")
            #print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(img_background, bbox, rt=0)

    #cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", img_background)
    cv2.waitKey(1)
