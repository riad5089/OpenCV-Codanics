# grayscale conversion
import cv2 as cv
from cv2 import cvtColor
img=cv.imread("resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg")
img=cv.resize(img,(800,600))
gray_img= cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("first_img",img)
cv.imshow("Gray_img",gray_img)
cv.waitKey(0)
cv.destroyAllWindows() #closes all windows