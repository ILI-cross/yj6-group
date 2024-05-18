import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# 저장된 모델 불러오기
model = load_model('mnist_model.h5')
print("Model loaded from disk.")

# 이미지 파일 로드
image_path = 'test.png'
image = Image.open(image_path).convert('L')  # 'L' 모드로 변환하여 그레이스케일 이미지로 만듦
image = image.resize((28, 28), Image.Resampling.LANCZOS)  # 이미지를 28x28로 리사이즈, LANCZOS 필터 사용

# 이미지 데이터 전처리
image_array = np.array(image)
image_array = image_array / 255.0  # 픽셀 값을 0~1 사이로 정규화
image_array = 1 - image_array  # MNIST 데이터는 배경이 검고 글자가 흰색이므로 반전시킴
image_array = image_array.reshape(1, 28, 28)  # 모델 입력을 위해 차원 확장

# 이미지 예측
prediction = model.predict(image_array)
predicted_label = np.argmax(prediction)

# 예측 결과 시각화
plt.imshow(image_array.reshape(28, 28), cmap='gray')  # 이미지 배열을 28x28로 변형하여 표시
plt.title(f'Predicted Label: {predicted_label}')
plt.axis('off')
plt.show()