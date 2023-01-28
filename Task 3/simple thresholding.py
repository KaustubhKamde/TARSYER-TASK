import cv2 
import numpy as np 

image1 = cv2.imread(r'C:\Users\ASUS\Downloads\Task_3.jpg') 
  

# convert the image in grayscale 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
  

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
  

# saving images
cv2.imwrite('Binary Threshold.jpg', thresh1)
cv2.imwrite('Binary Threshold Inverted.jpg', thresh2)
cv2.imwrite('Truncated Threshold.jpg', thresh3)
cv2.imwrite('Set to 0.jpg', thresh4)
cv2.imwrite('Set to 0 Inverted.jpg', thresh5)
      
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()
