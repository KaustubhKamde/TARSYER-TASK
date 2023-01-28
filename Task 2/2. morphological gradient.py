import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\ASUS\Desktop\Tarsyer\erosion1.png',0)
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('gradient_image',gradient)
cv.waitKey(0)
cv.destroyAllWindows()