#setting of camera or video
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
cap.set(10,100) # 10 is the key to set brightness
cap.set(3,1080) # width key 3
cap.set(4,1920) #height key 4

while True:
    ret,frame =cap.read()
    if ret==True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF==ord('q'): #0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
            break

        else:
            break

cap.release()
cv.destroyAllWindows()