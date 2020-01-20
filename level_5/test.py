#!/usr/bin/python3
from PIL import Image
import pytesseract
import cv2
import os
import argparse
import numpy as np
from subprocess import check_output

def cond_pic():
    path = "captcha.png"
    image = cv2.imread(path)
    scala = 80
    w = int(image.shape[1] * scala / 100)
    h = int(image.shape[0] * scala / 100)
    dim = (w, h)

    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #cv2.imwrite("hsv_img.png", hsv_img)
    #return "cond_cap.png"


    low = (0, 0, 128)
    high = (10, 10, 132)
    mask1 = cv2.inRange(hsv_img, low, high)
    low = (0, 0, 0)
    high = (124, 124, 124)
    mask2 = cv2.inRange(hsv_img, low, high)

    mask = cv2.bitwise_xor(mask1, mask2)
    target = cv2.bitwise_and(hsv_img, hsv_img, mask=mask)

    target = cv2.bitwise_not(target, target, mask=mask)

    cv2.imwrite("cond_cap_mask.png", mask)
    #cv2.imwrite("cond_cap.png", target)
    path = "cond_cap_mask.png"
    return pytesseract.image_to_string(Image.open(path))
    #cv2.imwrite("mask.png", mask)
    #cv2.imwrite("gray.png", image)

    
