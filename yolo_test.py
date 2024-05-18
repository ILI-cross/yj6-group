# pip install pillow

from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

# COCO 데이터 셋으로 사전 학습 된 모델이 다운로드 되고 로드 됨
model = YOLO("yolov8n.pt")  

# 대상 이미지를 로드
im1 = Image.open("mans.jpg")
# 예측 실행 - 결과는 이미지 파일로 저장됨
results = model.predict(source=im1, save=True)  # save plotted images

# 결과 출력 - List 형태
print(results)

