
""" Для проверки работоспособности камеры!!! """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print('camera error!')

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()