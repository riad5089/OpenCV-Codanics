#convert into different shapes of gray and black and white
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)

while(True):
    (ret,frame)=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh, b_w) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    cv.imshow("black_white",b_w)
    cv.imshow("Original",frame)
    cv.imshow("Gray", gray)
    if cv.waitKey(1) & 0xFF == ord('q'):  # 0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
        break

cap.release()
cv.destroyAllWindows()
