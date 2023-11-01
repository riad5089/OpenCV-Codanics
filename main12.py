#basic functions or manipulations in open cv
import cv2 as cv
import numpy as np
img=cv.imread("resources/2862c9da088557e1140068ed564f2307c63ba489a54363d44d19161c.jpg")

resized_img=cv.resize(img,(350,250))
#gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blurred image
blurr_img=cv.GaussianBlur(img,(23,23),0) #  kernel used for blur image

#edge detection
edge_img=cv.Canny(img,47,47) #theshold 48,48
#edge_img=cv.Canny(img,48,48)

# thickness of lines
mat_kernel =np.ones((7,7), np.uint8)
dilated_img=cv.dilate(edge_img,(mat_kernel),iterations=1)
# dilated_img=cv.dilate(edge_img,(7,7),iterations=1)




# cv.imshow("Original",img)

# cv.imshow("Resized", resized_img)
# cv.imshow("Gray", gray_img)
# cv.imshow("Blur", blurr_img)
cv.imshow("edge", edge_img)
cv.imshow("Dilated", dilated_img)





cv.waitKey(0)
cv.destroyAllWindows()