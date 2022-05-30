import cv2
import time
import glob
import os

currentWebcam = cv2.VideoCapture(0)


def takePicture(frame):
    image = "picture_{}.png".format(time.time())
    cv2.imwrite("imageLogs/" + image, frame)
    print("Image saved.")

def getLatestPictureFile():
    files = glob.iglob('imageLogs/*.png')
    try:
        latest = max(files, key=os.path.getctime)
    except ValueError:
        latest = "No files have been found - perhaps no files have been created yet?"

    return str(latest)