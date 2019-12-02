import cv2
import pytesseract
from PIL import Image
import numpy as np
import os
import han_spell2

img_path = '/home/pi/myProject/img_path/'
train_path = '/home/pi/myProject/ocr_train_path/'
result_path = '/home/pi/myProject/result_path/'

os.environ['TESSDATA_PREFIX'] = train_path

file_list = os.listdir(img_path)

for file_name in file_list:

    image = cv2.imread(img_path + file_name)

    height, width = image.shape[:2]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (width*3, height*3), interpolation=cv2.INTER_CUBIC)
    #gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,8)
    #gray = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]


img_new = Image.fromarray(gray)

result = han_spell2.spellchecker(pytesseract.image_to_string(img_new, lang='git_kor', config='-c preserve_interword_spaces=1'))
result = han_spell2.spellchecker(result)
result = han_spell2.spellchecker(result)

f = open("result.txt", 'w')
f.write(result.encode('utf-8'))
f.close()
