import cv2 as cv
import pyautogui

camera_index = 0

camera = cv.VideoCapture(camera_index)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')

while True:

    ret, frame = camera.read()

    if ret:

        face_detect = 0

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray, 1.1, 15, minSize=(10, 10))

        for (x, y, w, h) in face:
            cv.rectangle(img=frame, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=5)
            cv.putText(frame, "Face Detected", (x + 5, y + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            face_detect += 1

        if face_detect > 1:
            pyautogui.hotkey('winleft', 'l')

        cv.imshow("Stranger detection", frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv.destroyAllWindows()