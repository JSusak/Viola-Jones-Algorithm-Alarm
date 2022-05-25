import cv2
from scipy.misc import face
import time
import setup
import jsonLogger
import soundThreader
import imageGrabber


def main():
    eyeTrain = setup.initHaarFiles("haarcascade_eye")
    faceTrain = setup.initHaarFiles("haarcascade_frontalface_alt2")
    mouthTrain = setup.initHaarFiles("haarcascade_smile")

    cv2.namedWindow("Viola-Jones Algorithm Alarm (Josh)")
    webcam = cv2.VideoCapture(0)
    oldTime = time.time()


    # def setLiveTimer(frame):
    # threading.Timer(1,cv2.putText(frame, str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")), (0,25),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,2)).start()

    # setLiveTimer(webcam)

    while True:
        ret, frame = webcam.read()
        count = 0
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
                (255, 255, 255),
                3,
                cv2.LINE_AA,
            )
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
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
                    (255, 255, 0),
                    3,
                    cv2.LINE_AA,
                )
                frame = cv2.circle(frame, eye_center, radius, (255, 255, 0), 4)

            for (x3, y3, w3, h3) in mouth:
                cv2.putText(
                    frame,
                    "Smile :)",
                    (x + x3, y + y3 - 50),
                    cv2.FONT_ITALIC,
                    1,
                    (0, 255, 0),
                    3,
                    cv2.LINE_AA,
                )
                frame = cv2.rectangle(
                    frame, (x + x3, y + y3), (x + x3 + w3, y + y3 + h3), (0, 255, 0), 1
                )

        cv2.imshow("Viola-Jones Algorithm Alarm (Josh) [PRESS E TO EXIT]", frame)
        if time.time() - oldTime > 10:
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
