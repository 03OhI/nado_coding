"""
[활용편6 19] 사각 윤곽선 검출
- boundingRect : 윤곽선을 감싸는 최소 사각형의 (x, y, w, h)
- 모든 윤곽선을 사각형으로 감싸 위치를 표시한다.
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
contours, _ = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
for cnt in contours:
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(target, (x, y), (x + width, y + height), COLOR, 2)
    print("위치 ({}, {}) / 크기 {} x {}".format(x, y, width, height))

cv2.imshow("rect contours", target)
cv2.waitKey(0)
cv2.destroyAllWindows()
