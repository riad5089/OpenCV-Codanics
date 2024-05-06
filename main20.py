# how to detect specific colors inside python
#
import cv2 as cv
from cv2 import imshow
import numpy as np

img =cv.imread('resources/Image_gray.jpg')

# convert in hsv (Hue, Saturation, Value)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# sliders
def slider():
    pass

path='resources/Image_gray.jpg'

cv.namedWindow("Bars")
cv.resizeWindow("Bars",1000,500)

cv.createTrackbar("Hue Minimum","Bars",0,179,slider)
cv.createTrackbar("Hue Maximum","Bars",179,179,slider)
cv.createTrackbar("Saturation Minimum","Bars",0,255,slider)
cv.createTrackbar("Saturation Maximum","Bars",255,255,slider)
cv.createTrackbar("Value Minimum","Bars",0,255,slider)
cv.createTrackbar("Value Maximum","Bars",255,255,slider)

img =cv.imread(path)

# convert in hsv (Hue, Saturation, Value)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hue_min=cv.getTrackbarPos("Hue Minimum","Bars")
print(hue_min)

# cv.imshow("Original",img)
# cv.imshow("hsv img",hsv_img)

cv.waitKey(0)
cv.destroyAllWindows()



