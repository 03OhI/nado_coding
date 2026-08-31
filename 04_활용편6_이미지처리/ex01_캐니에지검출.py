"""
[활용편6 17] 경계선(에지) 검출 - 소벨과 캐니
- 에지 : 밝기가 급격하게 변하는 부분. 밝기 변화율(그레디언트)을 측정해 찾는다.
- 1차 미분(소벨) 만으로는 후보가 너무 많아 정확한 경계를 특정하기 어렵다.
- 캐니(Canny) : 가우시안 노이즈 제거 → 소벨로 기울기·방향 계산
                → 비최대 억제로 1픽셀까지 얇게 → 이중 임계값으로 강/약 에지 구분
"""
import cv2
import os
from _sample import make_sample

path = "sample.jpg"
if not os.path.exists(path):
    make_sample(path)

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 1차 미분 : 소벨 연산자 (x 방향, y 방향 기울기)
sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

# 캐니 에지 : (하위 임계값, 상위 임계값, 소벨 커널 크기, L2 norm 사용)
canny_low = cv2.Canny(img, 50, 150, apertureSize=3, L2gradient=True)
canny_high = cv2.Canny(img, 150, 250, apertureSize=3, L2gradient=True)

cv2.imshow("gray", img)
cv2.imshow("sobel x", sobel_x)
cv2.imshow("sobel y", sobel_y)
cv2.imshow("canny 50-150", canny_low)     # 임계값이 낮을수록 선이 많이 검출됨
cv2.imshow("canny 150-250", canny_high)
cv2.waitKey(0)
cv2.destroyAllWindows()
