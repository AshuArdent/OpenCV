# 5 essential functions in Opencv
import cv2 as cv

img = cv.imread("images/city.jpg")

cv.imshow("Chair", img)

# Converting to grayscal
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Blur Image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #ksize = kernel size 
# By increasing the ksize, it increase the blur
cv.imshow("Blur", blur)

#Edge Cascad
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dailating the image
dilate = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilate", dilate)

# Eroded Image
eroded = cv.erode(dilate, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (800, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resize)

# Cropped Image
crop = img[100:200, 200:400]
cv.imshow("Cropped", crop)

cv.waitKey(0)