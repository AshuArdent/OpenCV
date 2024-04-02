import cv2 as cv
import numpy as np

img = cv.imread("images/chair.jpg")

cv.imshow("Image",img)

#Translation

def translate(img, x, y):
    transMat = np.float64([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

#-x => left
#-y => up
#x => right
#y => down

trans = translate(img, -100, 100)
cv.imshow('translate', trans)

# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotat = rotate(img, 90)
cv.imshow('Rotated', rotat)

#Resize Image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resize)

#Flipping

#0 => vertical flip, 1 => horizontally, -1 => both

flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Cropping
crop = resize[200:300, 300:400]
cv.imshow('Crop', crop)

cv.waitKey(0)