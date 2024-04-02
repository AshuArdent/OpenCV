#Resizing and Rescaling the image and videos
import cv2 as cv

def rescalingFrame(frame, scale=0.75):
    # It is use for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

#Read video
capture = cv.VideoCapture("videos\demo.mp4") #it needs the video read by frame by frame

def changeRes(width, height):
    # It is use for live video
    capture.set(3, width)
    capture.set(4, height)

#we using while loop for caputring the video frame
while True:
    isTrue, Frame = capture.read()

    frame_resize = rescalingFrame(Frame, scale=.2)

    cv.imshow('Video', frame_resize) #show frame by frame

    if cv.waitKey(20) and 0xFF==ord('d'): #break the loop once d key press
        break

capture.release() #Release the video 
cv.destroyAllWindows() #destroy all working windows