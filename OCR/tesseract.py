import cv2
import pytesseract
from PIL import Image
import numpy as np
import os

img_for_tesseract_path = '/home/pi/myProject/img_path/'
train_path = '/home/pi/myProject/ocr_train_path'
save_path = '/home/pi/myProject/img_hanspell_path/'
os.environ['TESSDATA_PREFIX'] = train_path

file_list = os.listdir(img_for_tesseract_path)

def tesseract():

    for file_name in file_list:
        image = cv2.imread(img_for_tesseract_path + file_name)
        result = pytesseract.image_to_string(image, lang='tessdata_kor', config='-c preserve_interword_spaces=1')
        save_file_name = file_name[0:-4]
        f = open(save_path+save_file_name+'.txt', 'w')
        f.write(result.encode('utf-8'))
        f.close()

