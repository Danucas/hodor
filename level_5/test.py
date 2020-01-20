#!/usr/bin/python3
from PIL import Image
import pytesseract
import cv2
import os
import argparse
import numpy as np

def cond_pic():
    image = cv2.imread('captcha.png')
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("cond_cap.png", hsv_img)
    return "cond_cap.png"


    #low = np.array([0, 0, 0], dtype = 'uint16')
    #high = np.array([70, 70, 70], dtype = 'uint16')
    #mask = cv2.inRange(image, low, high)

    #image = cv2.bitwise_and(image, image, mask=mask)

    #cv2.imwrite("mask.png", mask)
    #cv2.imwrite("gray.png", image)
    
