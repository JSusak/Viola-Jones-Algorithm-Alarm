#All neccessary imports.
import cv2
from scipy.misc import face
import time
import requests
import setup
import imutils
import jsonLogger
import soundThreader
import imageGrabber
from datetime import datetime
from datetime import timedelta
from timeit import default_timer as timer
import numpy as np
import sqliteManager
import CONSTANTS
import colourFilters

#Get the constants found in CONSTANTS.py
INTERVAL = CONSTANTS.INTERVAL

COLOUR = CONSTANTS.COLOUR

URL = CONSTANTS.APPURL

timeElapsed = 0



def start(phoneMode):
    if(phoneMode):
        if(URL==None):
            print("You are liar men. You didn't put a url to the 'IP Webcam' environment.")
            return
    #Retrieve the haar cascade files, preparing them for the program to use.
    eyeTrain = setup.initHaarFiles("haarcascade_eye")
    faceTrain = setup.initHaarFiles("haarcascade_frontalface_alt2")
    mouthTrain = setup.initHaarFiles("haarcascade_smile")

    cv2.namedWindow("Viola-Jones Algorithm Set-up")
    
    #Get a reference to the main webcam as well as the current time of execution.
    if(not phoneMode):
        global webcam 
        webcam = cv2.VideoCapture(0)

    oldTime = time.time()
    initialTime = timer();


    #Infinite loop used to gather camera information on a frame-by-frame basis.
    while True:
        if(phoneMode):

            #The problem I see with linking your android device is that the IP webcam site is INSECURE.
            #The only way for the code to run properly is to add another parameter to not check the certificates of the site.
            #I shall comment this out so if you want to use an android device you will have to uncomment this line.
            #If you get attacked (highly unlikely) I have warned you !! 

            frame = requests.get(URL),# verify=False)
            img_arr = np.array(bytearray(frame.content), dtype=np.uint8)
            frame = cv2.imdecode(img_arr, -1)
            frame = imutils.resize(frame, width=1000, height=1800)
        else:
            ret, frame = webcam.read()
            frame = imutils.resize(frame, width=1000, height=1800)
        cv2.putText(
            frame,
            'Current time: {}'.format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
            (0, 25),
            cv2.FONT_ITALIC,
            1,
            COLOUR if COLOUR is not None else (255, 255, 255),
            1,
            2,
        )
        cv2.putText(
            frame,
            "SPACE = take a snapshot. E = exit :)",
            (0, 745),
            cv2.FONT_ITALIC,
            1,
            COLOUR if COLOUR is not None else (255, 255, 255),
            1,
            2,
        )
        gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Get current info.
        if cv2.waitKey(1) & 0xFF is ord("x"):
            getInfo()

        #while cv2.waitKey(1) & 0xFF is ord("r"):
            #colourFilters.invertImage(frame)

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
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                COLOUR if COLOUR is not None else (255, 255, 255),
                2,
            )
            faceDetected = frame[y : y + h, x : x + w]
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
                frame = cv2.circle(
                    frame,
                    eye_center,
                    radius,
                    COLOUR if COLOUR is not None else (255, 255, 0),
                    4,
                )

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
                    frame,
                    (x + x3, y + y3),
                    (x + x3 + w3, y + y3 + h3),
                    COLOUR if COLOUR is not None else (0, 255, 0),
                    1,
                )

        cv2.imshow("Viola-Jones Algorithm Alarm [Josh]", frame)
        #User can press the space bar OR wait for the chosen interval to pass.
        #Keep in mind that pressing the spacebar also resets the interval.
        if ((time.time() - oldTime > INTERVAL) or (cv2.waitKey(1) & 0xFF is ord(" "))):
            soundThreader.playSound("capture", "wav")
            print("Snapshot of current frame stored for processing.")
            timeElapsed =  timer() - initialTime
            #If the length of the faceDetection tuple is 0, no positions are being logged, therefore meaning there is no face present.
            if len(faceDetection) == 0:
                print(
                    "WARNING: No face found. Nothing has been saved to JSON or image logs."
                )
                oldTime = time.time()
            else:
                oldTime = time.time()


                #If a face HAS been found, take a picture, play the siren sound, insert into the database...
                imageGrabber.takePicture(frame)
                soundThreader.playSound("siren", "mp3")
                jsonLogger.replaceLogs(faceDetection)
                sqliteManager.insertIntoFaces(jsonLogger.getLastDetectedID(),datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                sqliteManager.insertIntoFacesLink(jsonLogger.getLastDetectedID(),imageGrabber.getLatestPictureFile())

                print(
                    "Face has been found. Saved into image logs and logging position + last seen date into JSON/db file."
                )

                getInfo()


        if cv2.waitKey(1) & 0xFF is ord("e"):
            print(
                "Recording has been terminated. Thanks for experimenting with the algorithm!"
            )
            break

    if(not phoneMode):
        webcam.release()
        
    cv2.destroyAllWindows()

def quit():
    webcam.release()       
    cv2.destroyAllWindows()

def getInfo():
    print("---------------MOST RECENT LOGS---------------")
    print("----------CURRENT JSON STATS----------")
    #Logs read from the json file...
    print(jsonLogger.readLogs())
    print("----------CURRENT SQLITE DB STATS----------")
    #Alongside the database!
    sqliteManager.getLastRowFaces()
    sqliteManager.getLastRowFacesLink()

    print("TOTAL TIME ELAPSED: " + str(timedelta(seconds=timeElapsed)))

