
#how to capture a webcam inside python
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0) #webcam no 1
# if (cap.isOpened() ==False):
#     print("There is an error")
#read untill the end
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("Frame",frame)
        if cv.waitKey(1) & 0xFF==ord('q'): #0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

