import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist

# 데이터 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0

# 저장된 모델 불러오기
model = load_model('mnist_model.h5')
print("Model loaded from disk.")

# 테스트 데이터셋에서 랜덤 이미지 선택
random_index = np.random.randint(0, x_test.shape[0])
random_test_image = x_test[random_index]
random_test_label = y_test[random_index]

# 이미지 예측
random_test_image_expanded = np.expand_dims(random_test_image, axis=0)  # 모델 입력을 위해 차원 확장
prediction = model.predict(random_test_image_expanded)
predicted_label = np.argmax(prediction)
print(predicted_label)

# 예측 결과 시각화
plt.imshow(random_test_image, cmap='gray')
plt.title(f'Predicted: {predicted_label}, Actual: {random_test_label}')
plt.axis('off')
plt.show()