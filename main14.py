# Resolution of cam

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
# resolution hd(1280,720)

def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)


def find_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)


# hd_resolution()
# sd_resolution()
find_resolution()
while(True):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("Camera",frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break


    else:
        break

cap.release()

cv.destroyAllWindows()
