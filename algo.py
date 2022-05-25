import cv2
from scipy.misc import face
import time
import setup
import jsonLogger
import soundThreader
import imageGrabber
from datetime import datetime

#Change this value to modify the interval at which frames are inspected.
INTERVAL = 30;
#Change this variable to modify the universal colour of all shapes in the program. You can also choose to leave it as None, providing random colours.
#Put in the form (g,b,r) otherwise program will crash!
COLOUR = (0,23,250)

def main():
    eyeTrain = setup.initHaarFiles("haarcascade_eye")
    faceTrain = setup.initHaarFiles("haarcascade_frontalface_alt2")
    mouthTrain = setup.initHaarFiles("haarcascade_smile")

    cv2.namedWindow("Viola-Jones Algorithm Alarm (Josh)")
    webcam = cv2.VideoCapture(0)
    oldTime = time.time()

    while True:
        ret, frame = webcam.read()
        cv2.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (0,25),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1, COLOUR if COLOUR is not None else (255,255,255),1,2)
        gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faceDetection = faceTrain.detectMultiScale(
            gs,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        for (x, y, w, h) in faceDetection:
            cv2.putText(
                frame,
                "Face",
                (x, y - 50),
                cv2.FONT_ITALIC,
                2,
                COLOUR if COLOUR is not None else (255, 255, 255),
                3,
                cv2.LINE_AA,
            )
            cv2.rectangle(frame, (x, y), (x + w, y + h), COLOUR if COLOUR is not None else (255, 255, 255), 2)
            faceDetected = frame[y : y + h, x : x + w]
            faceDetectedGrey = gs[y : y + h, x : x + w]
            eyes = eyeTrain.detectMultiScale(faceDetected)
            mouth = mouthTrain.detectMultiScale(faceDetected)
            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                radius = int(round((w2 + h2) * 0.25))
                cv2.putText(
                    frame,
                    "Eye",
                    (x + x2, y + y2 - 50),
                    cv2.FONT_ITALIC,
                    1,
                    COLOUR if COLOUR is not None else (255, 255, 0),
                    3,
                    cv2.LINE_AA,
                )
                frame = cv2.circle(frame, eye_center, radius, COLOUR if COLOUR is not None else (255, 255, 0), 4)

            for (x3, y3, w3, h3) in mouth:
                cv2.putText(
                    frame,
                    "Smile :)",
                    (x + x3, y + y3 - 50),
                    cv2.FONT_ITALIC,
                    1,
                    COLOUR if COLOUR is not None else (0, 255, 0),
                    3,
                    cv2.LINE_AA,
                )
                frame = cv2.rectangle(
                    frame, (x + x3, y + y3), (x + x3 + w3, y + y3 + h3), COLOUR if COLOUR is not None else (0, 255, 0), 1
                )

        cv2.imshow("Viola-Jones Algorithm Alarm (Josh) [PRESS E TO EXIT]", frame)
        if time.time() - oldTime > INTERVAL:
            soundThreader.playSound("capture", "wav")
            print("Snapshot of current frame stored for processing.")
            if len(faceDetection) == 0:
                print(
                    "WARNING: No face found. Nothing has been saved to JSON or image logs."
                )
                oldTime = time.time()
            else:
                oldTime = time.time()
                print(jsonLogger.readLogs())
                imageGrabber.takePicture(frame)
                soundThreader.playSound("siren", "mp3")
                jsonLogger.replaceLogs(faceDetection)
                print(
                    "Face has been found. Saved into image logs and logging position and last seen date into JSON."
                )

        if cv2.waitKey(1) & 0xFF is ord("e"):
            print(
                "Recording has been terminated. Thanks for experimenting with the algorithm!"
            )
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
