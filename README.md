# Hallym University [시스템 프로그래밍]
## Subject
#### RasberryPi 4 Cluster, Tesseract, OpenCV, Py-hanspell 을 이용하여 
#### 사진속의 텍스트를 디지털 텍스트로 변환후 맞춤법 검사하기
## Developer
#### 조명근(영상처리, Tesseract) 
#### 이용하(클러스터 구성 및 맞춤법 검사) 
#### 노영진(아날로그데이터 수집 및 영상처리)
## 사용한 오픈소스
#### Tesseract : https://github.com/tesseract-ocr/tesseract
#### OpenCV 4.1.2 : https://github.com/opencv
#### 네이버 맞춤법 검사기
## Project Info
#### 사진 속의 텍스트를 디지털 텍스트로 변환한 뒤에 인식률을 높이기 위해서 OpenCV를 사용해 이미지를 전처리하고, 전처리한 이미지를 Tesseract를 사용해 디지털 텍스트로 변한한다.마지막으로, 네이버 맞춤법 검사기를 사용해 맞춤법까지 검사한다.
#### 클러스터는 전반적인 연산을 담당하며 낮은 가격에 최대한의 효율을 도출해 내기 위해 구성하였다. 
## Project Result
#### 프로젝트 다이어그램
![다이어그램](https://user-images.githubusercontent.com/50908416/69917891-6d5e8f00-14ae-11ea-98cc-e374f0e56e63.png)
#### 원본 파일
![원본](https://user-images.githubusercontent.com/50908416/69917893-6df72580-14ae-11ea-84a7-58eed32f9519.jpg)
#### 전처리 후 파일
![전처리](https://user-images.githubusercontent.com/50908416/69917894-6e8fbc00-14ae-11ea-8643-b1f7602b5f32.PNG)
#### 결과물
![최종 결과](https://user-images.githubusercontent.com/50908416/69917896-6fc0e900-14ae-11ea-9e3c-b2b6ec21fe95.PNG)
## 프로젝트 사용 방법
#### OpenCV와 pytesseract가 설치되어있어야 합니다.
#### 1.디지털 텍스트로 변환하고 싶은 이미지를 프로젝트 폴더에 삽입 
#### 2.OCR.py 파일을 실행하여, 밑줄친 부분을 이미지 이름으로 변경
![밑줄](https://user-images.githubusercontent.com/50908416/69917987-e4485780-14af-11ea-8a27-e01406927058.PNG)
#### 3.F5버튼을 클릭해 실행

