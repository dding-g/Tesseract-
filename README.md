# Hallym University [시스템 프로그래밍]
## Subject
#### RasberryPi 4 Cluster, Tesseract, OpenCV, Py-hanspell 을 이용하여 사진속의 텍스트를 디지털 텍스트로 변환후 맞춤법 검사하기
## Developer
#### 조명근(영상처리, Tesseract) 
#### 이용하(클러스터 구성 및 맞춤법 검사) 
#### 노영진(아날로그데이터 수집 및 영상처리)
## 사용한 오픈소스
#### Tesseract : https://github.com/tesseract-ocr/tesseract
#### OpenCV 4.1.2 : https://github.com/opencv
#### 네이버 맞춤법 검사기
## Project Info
#### 사진 속의 텍스트를 디지털 텍스트로 변환한 뒤에 인식률을 높이기 위해서 OpenCV를 사용해 이미지를 전처리한다.
#### 그 다음, 전처리한 이미지를 Tesseract를 사용해 디지털 텍스트로 변한한다.
#### 마지막으로, 네이버 맞춤법 검사기를 사용해 맞춤법까지 검사한다.



