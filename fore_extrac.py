# Background Subtraction using OpenCV 
import numpy as np 
import cv2 

cap = cv2.VideoCapture(0) 
bgs = cv2.createBackgroundSubtractorMOG2() 

while(1): 
	ret, frame = cap.read() 

	fmask = bgs.apply(frame) 

	cv2.imshow('Input', frame) 
	cv2.imshow('Foreground', fmask) 

	
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break
	

cap.release() 
cv2.destroyAllWindows() 

