# Draw and Write on image
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8") 
# (500, 500, 3) => (width, height, number of color channel)
# uint8 is the data type of the image and here i am creating the blank image
# 

# cv.imshow("blank", blank)

# 1 Paint the image a ceratin color
# blank[:] = 0,255,0

# Paint certain section on the image
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Green", blank)

#2) Draw a Rectangle 
# cv.rectangle(blank, (200,200), (350,350), (0,255,0), thickness=2)
# cv.imshow("Green", blank)

# 3) Draw center

# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow("Circle", blank)

#4) Draw line
# cv.line(blank, (50,50), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=1)
# cv.imshow("Line", blank)

#5) Write text on image
cv.putText(blank, "I am the color green.", (100,100), cv.FONT_HERSHEY_TRIPLEX, .5, (0,255,0), thickness=1)
cv.imshow("Text", blank)

cv.waitKey(0)