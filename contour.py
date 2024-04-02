# Contour Detection
# Contour is basically boundries of the object. It si use for shape analysis and object detection and recognigation. 
import cv2 as cv

img = cv.imread("images/chair.jpg")

cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

cany = cv.Canny(blur, 125, 175)
cv.imshow('Cany', cany)

# ret, thresold = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresold)

contours, heirerchy = cv.findContours(cany, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours length, {len(heirerchy)} heirerchy length')

cv.waitKey(0)
