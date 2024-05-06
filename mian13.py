# how to draw lines and shape in python

import cv2 as cv
import numpy as np

# Draw a canvas o is for black
img=np.zeros((600,600))
print("The size of canvsas is: ",img.shape)
# print(img)
# adding colors to the canvas
colored_img=np.zeros((600,600,3),np.uint8) #color channel addition
colored_img[:]= 255,0,255 #color key
colored_img[150:230,100:207]= 255,168,20  #part of to be colored


# adding line
cv.line(colored_img,(100,100),(300,300),(255,255,0),3)
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)



#adding ractagles
# cv.rectangle(colored_img, (50,100), (255,240,0),3)
cv.rectangle(colored_img, (50, 100), (255, 240), 3)
cv.rectangle(colored_img, (50, 100), (255, 255),cv.FILLED) #fill rectangle

# adding circle
cv.circle(colored_img, (400,300),50,(255,100,0),5)

cv.circle(colored_img, (400,300),50,(255,100,0),cv.FILLED)

#adding text

cv.putText(colored_img,"Kese Hoo Vai",(200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),2)



# 1 is for white

# img1=np.ones((600,600))
#
# cv.imshow("Black",img)
# cv.imshow("White",img1)
cv.imshow("colored image",colored_img)

cv.waitKey(0)
cv.destroyAllWindows()