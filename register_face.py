import face_recognition
import cv2
import numpy as np

# Capture the Video Cam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    raise IOError("Cannot open webcam")

# Load the image and encode
jawed_image = face_recognition.load_image_file("data_face/jawed1.jpeg")
jawed_face_encoding = face_recognition.face_encodings(jawed_image)
if not jawed_face_encoding:
    raise ValueError("No Face Found in jawed1.jpeg")
jawed_face_encoding = jawed_face_encoding[0]

# Load Munzilin image
munz_image = face_recognition.load_image_file("data_face/munz3.jpeg")
munz_face_encoding = face_recognition.face_encodings(munz_image)[0]

known_faces_encoded = [
    jawed_face_encoding,
    munz_face_encoding
]

known_faces_name = [
    "Jawed",
    "Munzilin"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces_encoded, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_faces_name[first_match_index]

            face_distances = face_recognition.face_distance(known_faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_faces_name[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

            # Displaying the result
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        left *= 4
        bottom *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display result Image
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
