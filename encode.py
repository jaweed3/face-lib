import cv2
import face_recognition
import pickle
import os

folderPath = 'data_face'
modePathList = os.listdir(folderPath)
imgList = []

student_ids = []
for path in modePathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    student_ids.append(os.path.splitext(path)[0])
    #print(path)
    #print(os.path.splitext(path))
print(student_ids)

def findEncoding(images_list):
    encodeList = []
    for img in images_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding started...")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, student_ids]
print("Encoding Completed")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved....")
