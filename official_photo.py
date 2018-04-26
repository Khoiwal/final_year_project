import cv2
import os
import face_recognition
import config



name = input("Enter name: ")

if name == None or len(name) < 1:
    raise ("what's your name? ")

cap = cv2.VideoCapture(0)
if not os.path.exists(config.CHECK_FACE_FOLDER):
    os.makedirs(config.CHECK_FACE_FOLDER)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera error!")

    small_face = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    face_location = face_recognition.face_locations(small_face)

    if len(face_location) > 1:
        cv2.putText(frame, 'please ensure there is only one person in the picture!', (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
    elif len(face_location) == 1:
            # status = True
        cv2.putText(frame, 'please, press key "c" to take photo!', (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
    else:
        cv2.putText(frame, 'no face detected!', (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
    cv2.imshow('', frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        print('quit!')
        break
    elif k & 0xFF == ord('c'):
        print(name + " has been added successfully!")
        cv2.imwrite(config.CHECK_FACE_FOLDER + name + '.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()



