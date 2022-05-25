import cv2


def initHaarFiles(cascadeName):
    print(cascadeName + " loaded.")
    return cv2.CascadeClassifier(cv2.data.haarcascades + cascadeName + ".xml")
