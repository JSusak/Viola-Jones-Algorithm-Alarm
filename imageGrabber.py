import cv2
import time
currentWebcam = cv2.VideoCapture(0)

def takePicture(frame):
    image = "picture_{}.png".format(time.time())
    cv2.imwrite('resources/'+image, frame)
    print("Image saved.")