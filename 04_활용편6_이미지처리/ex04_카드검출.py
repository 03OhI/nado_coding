"""
[활용편6 20] 카드 검출 (조건으로 원하는 윤곽선만 걸러내기)
- area         : contourArea 로 구한 넓이
- aspect_ratio : 가로 / 세로 비율
- 넓이와 비율 조건을 동시에 만족하는 윤곽선만 카드로 판단한다.
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

COLOR = (0, 0, 255)
idx = 1
for cnt in contours:
    area = cv2.contourArea(cnt)
    x, y, width, height = cv2.boundingRect(cnt)
    aspect_ratio = float(height) / width if width else 0

    # 넓이와 가로세로 비율이 카드 범위에 들어올 때만 선택
    if 1000 < area < 50000 and 1.2 < aspect_ratio < 1.7:
        cv2.rectangle(target, (x, y), (x + width, y + height), COLOR, 2)
        crop = img[y:y + height, x:x + width]
        cv2.imshow("card {}".format(idx), crop)   # 검출한 카드만 잘라서 표시
        cv2.imwrite("card_{}.png".format(idx), crop)
        idx += 1

print("검출한 카드 개수 :", idx - 1)
cv2.imshow("detected", target)
cv2.waitKey(0)
cv2.destroyAllWindows()
