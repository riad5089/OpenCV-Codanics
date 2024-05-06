import cv2 as cv
import numpy as np
img=cv.imread("resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg")

resized_img=cv.resize(img,(350,250))
print("The size of out image is: ", img.shape)
cropped_img=resized_img[0:400,0:300] #height and width


cv.imshow("Original",img)

cv.imshow("cropped",cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()