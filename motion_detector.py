import cv2
import time


first_frame = None

video = cv2.VideoCapture(0)


while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    compare_frame = cv2.absdiff(first_frame, gray)

    cv2.imshow('Gray', gray)
    cv2.imshow('compare', compare_frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows
