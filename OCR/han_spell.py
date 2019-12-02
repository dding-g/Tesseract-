#-*- coding:utf-8 -*-
import json
import re
import requests
import os

tesseract_path = '/home/pi/myProject/img_hanspell_path/'
result_path = '/home/pi/myProject/result_path/'
file_list = os.listdir(tesseract_path)
data = ''
url = "https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy"
params = {
           '_callback': 'jQuery',
            'q' : '',
            'where' : 'nexearch',
            'color_blindness' :'0',
            '_' : '1575208518671',
         }   
def set_params(data):
    global params
    
    params['q'] = data
    response = requests.get(url, params=params).text
    response = response.replace(params['_callback'] + '(', '')
    response = response.replace(');', '')
    response_dict = json.loads(response, encoding='utf-8')
    result_text = response_dict['message']['result']['html']
    result_text = re.sub(r'<\/?.*?>', '', result_text)
    
    return result_text

def han_task():
    for file_name in file_list:
        f = open(tesseract_path + file_name, 'r')
        data = f.read()
        f.close()
        
        for i in range(0,3):
            data = set_params(data)
        
        hangul_reg = re.compile('[^ ㄱ-ㅣ가-힣]+')
        data = hangul_reg.sub(' ', data)
        f = open(result_path + file_name, 'w')
        f.write(data.encode('utf-8'))
        f.close()



