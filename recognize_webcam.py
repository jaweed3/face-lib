import face_recognition
import cv2
import pickle

def recognize_from_webcam(faces_file="faces.pkl"):
    with open(faces_file, "rb") as f:
        known_faces = pickle.load(f)

    known_names = list(known_faces.keys())
    known_encodings = list(known_faces.values())

    cap = cv2.VideoCapture(0)
    print("[INFO] Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                matched_idx = matches.index(True)
                name = known_names[matched_idx]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow("Live Recognition - Press q to quit", frame)

        if cv2.waitKey(1) & 0xFF == ('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_from_webcam()
