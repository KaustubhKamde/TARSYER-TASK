import cv2 
import numpy as np 
    
image1 = cv2.imread(r'C:\Users\ASUS\Downloads\Task_3.jpg') 

#  convert the image in grayscale 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
   
# applying different thresholding 
# techniques on the input image
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 199, 5)
  
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 199, 5)
  
cv2.imwrite('Adaptive Mean.jpg', thresh1)
cv2.imwrite('Adaptive Gaussian.jpg', thresh2)
   
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()
