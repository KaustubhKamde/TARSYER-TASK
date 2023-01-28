import cv2

# Load the image
img = cv2.imread(r'C:\Users\ASUS\Desktop\Tarsyer\Task_1.jpg')

# Allow the user to select a rectangular region of the image
r = cv2.selectROI(img)

# Crop the image to the selected region
cropped_img = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Save the cropped image
cv2.imwrite("Task_1_cropped.jpg", cropped_img)

# Draw a rectangle on the original image to indicate the selected region
cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[0] + r[2]), int(r[1] + r[3])), (0, 0, 255), 2)

# Add the coordinates of the top-left and bottom-right corners to the image
cv2.putText(img, f'Top Left: ({r[0]}, {r[1]})', (int(r[0]), int(r[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.putText(img, f'Bottom Right: ({r[0]+r[2]}, {r[1]+r[3]})', (int(r[0]), int(r[1]+r[3])+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Save the image with the rectangle drawn on it
cv2.imwrite("Task_1_insights.jpg", img)

# Close the window
cv2.destroyAllWindows()