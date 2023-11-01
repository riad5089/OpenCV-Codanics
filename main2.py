#resize image
import cv2 as cv
img=cv.imread("resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg")
img1=cv.resize(img,(800,600))
cv.imshow("first_img",img)
cv.imshow("second_img",img1)
cv.waitKey(0)
cv.destroyAllWindows() #closes all windows