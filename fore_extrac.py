# Background Subtraction using OpenCV 
import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) 
bgs = cv2.createBackgroundSubtractorMOG2() 

while(1): 
	ret, frame = cap.read() 
	fmask = bgs.apply(frame) 

	ret, threshold = cv2.threshold(fmask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 
    
	kernel = np.ones((5,5),np.uint8)
	e = cv2.dilate(fmask,kernel,iterations = 1)

	cv2.imshow('Input', frame) 
	cv2.imshow('Foreground', fmask)	

	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break
	

cap.release() 
cv2.destroyAllWindows() 

