import cv2
def invertImage(frame):
    print("Image inverted...")
    return cv2.bitwise_not(frame);