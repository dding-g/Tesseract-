import cv2
from PIL import Image
import numpy as np
import os

img_path = '/home/pi/myProject/img_path/'
img_tesseract_path = '/home/pi/myProject/img_tesseract_path/'

file_list = os.listdir(img_path)

def img_pre():
    for file_name in file_list:
    
        image = cv2.imread(img_path + file_name)
    
        height, width = image.shape[:2]
    
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (width*3, height*3), interpolation=cv2.INTER_CUBIC)
        #gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,8)
        #gray = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
    
        save_img = Image.fromarray(gray)
        save_img.save(img_tesseract_path+file_name)
