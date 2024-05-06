#joining two images
import cv2 as cv
import numpy as np
img=cv.imread('resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg')

#stacking same image

# horizontal stack

# hor_img=np.hstack((img,img))

#vertical stack

ver_stack=np.vstack((img,img))
new_width = 500
new_height = 500
resized_ver_stack = cv.resize(ver_stack, (new_width, new_height))

# cv.imshow("Horizontal",hor_img)
cv.imshow("vertical",resized_ver_stack)
cv.waitKey(0)
cv.destroyAllWindows()