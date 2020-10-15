#!/usr/bin/python3
# -*- coding: utf-8 -*

import cv2
import numpy as np

fname='input.jpg'
threshold=220 


img_color= cv2.imread(fname) 
img_gray = cv2.imread(fname,cv2.IMREAD_GRAYSCALE) 
img_blur = cv2.blur(img_gray,(9,9)) 

ret, img_binary= cv2.threshold(img_blur, threshold, 255, cv2.THRESH_BINARY_INV) 
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
contours.sort(key=lambda x: cv2.contourArea(x), reverse=True)
rect = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(rect)
box = np.int0(box)

img3 = img_color[box[2][1]:box[0][1],box[1][0]:box[0][0]]
cv2.imwrite('output.png',img3)

print("Completed!")
