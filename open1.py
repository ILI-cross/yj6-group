# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# 데이터 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 이미지를 무작위로 선택
#random_index = np.random.randint(0, x_train.shape[0])
random_index = 5
# random_index = 0 # 0번째 이미지 선택
random_image = x_train[random_index]
random_label = y_train[random_index]

# 이미지 시각화
plt.figure(figsize=(5, 5))  # 이미지 크기 설정
plt.imshow(random_image, cmap='gray')  # 흑백 이미지로 표시
plt.title(f'Label: {random_label}')  # 이미지 위에 레이블 표시
plt.colorbar()  # 색상 바 추가
plt.axis('off')  # 축 끄기
plt.show()