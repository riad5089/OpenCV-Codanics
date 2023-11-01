#image into black and whtie image
import cv2 as cv
img=cv.imread('resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,b_w)=cv.threshold(gray,127,255,cv.THRESH_BINARY) #binary black and white
cv.imshow('Original',img)
cv.imshow("Gray",gray)
cv.imshow("Black_and_White",b_w)
cv.waitKey(0)
cv.destroyAllWindows()