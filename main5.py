#image saving an image writing images

import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
img=cv.imread('resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,b_w)=cv.threshold(gray,127,255,cv.THRESH_BINARY) #binary black and white

# b_w=cv.resize(b_w,(400,600))
imwrite("resources/Image_b_w.jpg",b_w)

imwrite("resources/Image_gray.jpg",gray)
# cv.waitKey(0)
# cv.destroyAllWindows()