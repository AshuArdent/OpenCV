import cv2 as cv

# #read the image
# img = cv.imread("images/chair.jpg")

# #show image
# cv.imshow('chair', img)

# cv.waitKey(0) # Wait for key press

#Read video
capture = cv.VideoCapture("videos\demo.mp4") #it needs the video read by frame by frame

#we using while loop for caputring the video frame
while True:
    isTrue, Frame = capture.read()

    cv.imshow('Video', Frame) #show frame by frame

    if cv.waitKey(20) and 0xFF==ord('d'): #break the loop once d key press
        break

    '''
    waitkey() function of Python OpenCV allows users to display a window for given milliseconds 
    or until any key is pressed. It takes time in milliseconds as a parameter and waits for the 
    given time to destroy the window, if 0 is passed in the argument it waits till any key is pressed. 
    '''

capture.release() #Release the video 
cv.destroyAllWindows() #destroy all working windows

'''
error: (-215:Assertion failed) - 
Video frame either not getting properly 
or video goes out of the frame size 
or video path not found

'''