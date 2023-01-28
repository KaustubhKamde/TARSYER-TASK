import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\Tarsyer\erosion1.png',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow('dilated_image',dilation)
cv.waitKey(0)
cv.destroyAllWindows()