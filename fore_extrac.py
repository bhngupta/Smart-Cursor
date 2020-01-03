# Background Subtraction using OpenCV 
import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) 
bgs = cv2.createBackgroundSubtractorMOG2() 

while(1): 
    ret, frame = cap.read() 
    frame = cv2.flip(frame, 1)
    fmask = bgs.apply(frame) 

    ret, threshold = cv2.threshold(fmask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 
    
    kernel = np.ones((5,5),np.uint8)
    e = cv2.dilate(fmask,kernel,iterations = 1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    
    contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Input', frame) 
    #cv2.imshow('Foreground', fmask)
    cv2.imshow('Edges', edged)
    

    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
    

cap.release() 
cv2.destroyAllWindows() 
