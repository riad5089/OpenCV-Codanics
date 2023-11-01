#basic functions or manipulations in open cv
import cv2 as cv
img=cv.imread("resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg")





cv.imshow("Original",img)
# cv.imshow("frame", img)

cv.waitKey(0)
cv.destroyAllWindows()