import cv2
def invertImage(frame):
    print("Image inverted...")
    return cv2.bitwise_not(frame);

def sepiaImage(frame):
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    frame_h,frame_w,frame_c = frame.shape
    frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
    return frame