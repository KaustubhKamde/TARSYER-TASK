import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\Tarsyer\erosion1.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
cv.imshow('eroded_image',erosion)
cv.waitKey(0)
cv.destroyAllWindows()