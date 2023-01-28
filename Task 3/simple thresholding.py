import cv2 
import numpy as np 
  
# path to input image is specified and  
# image is loaded with imread command 
image1 = cv2.imread(r'C:\Users\ASUS\Downloads\Task_3.jpg') 
  
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  
# applying different thresholding 
# techniques on the input image
# all pixels value above 120 will 
# be set to 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
  
# the window showing output images
# with the corresponding thresholding 
# techniques applied to the input images
cv2.imwrite('Binary Threshold.jpg', thresh1)
cv2.imwrite('Binary Threshold Inverted.jpg', thresh2)
cv2.imwrite('Truncated Threshold.jpg', thresh3)
cv2.imwrite('Set to 0.jpg', thresh4)
cv2.imwrite('Set to 0 Inverted.jpg', thresh5)
    
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()