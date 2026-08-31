"""
[활용편6 18] 윤곽선(Contour) 검출
- 그레이스케일 : 0~255 명도만 남긴 1차원 정보로 변환
- 오츠(Otsu)   : 최적의 임계값을 자동으로 찾아 흑백을 나누는 알고리즘
- findContours : 이진화로 만들어진 점들을 이어 닫힌 도형으로 묶는다.
                 결과는 이미지가 아니라 (x, y) 좌표 배열이다.
  · RETR_LIST         : 부모/자식 계층 구조를 무시하고 모두 단순 나열
  · CHAIN_APPROX_NONE : 모든 좌표를 저장 (정확하지만 메모리를 많이 사용)
"""
import cv2
import os
from _sample import make_sample

path = "sample.jpg"
if not os.path.exists(path):
    make_sample(path)

img = cv2.imread(path)
target = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("오츠 알고리즘이 찾은 임계값 :", ret)

contours, hierarchy = cv2.findContours(
    otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print("검출된 윤곽선 개수 :", len(contours))

# 찾은 윤곽선을 초록색으로 그린다
cv2.drawContours(target, contours, -1, (0, 255, 0), 2)

cv2.imshow("otsu", otsu)
cv2.imshow("contours", target)
cv2.waitKey(0)
cv2.destroyAllWindows()
