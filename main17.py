# how to change the perspective of image

# import cv2 as cv
# import numpy as np
#
# img=cv.imread('resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg')
#
# print(img.shape)
# #defining points
# point1=np.float32([[233,196],[522,169],[715,482]])
# width=1000
# height=957
#
# point2=np.float32([[0,0],[800,0],[0,height],[width,height]])
# matrix=cv.getPerspectiveTransform(point1,point2)
# out_img=cv.warpPerspective(img,matrix,(width,height))
#
# cv.imshow('Orginal',img)
# # cv.imshow('transformed',out_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img = cv.imread('resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg')

print(img.shape)

# Defining points
point1 = np.float32([[233, 196], [522, 169], [715, 482]])
width = 1000
height = 957
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Ensure the points are in the correct format
point1 = point1.reshape(-1, 1, 2)
point2 = point2.reshape(-1, 1, 2)

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('Original', img)
cv.imshow('Transformed', out_img)
cv.waitKey(0)
cv.destroyAllWindows()

