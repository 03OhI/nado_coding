"""테스트용 이미지 생성 (별도 이미지 파일이 없어도 예제를 실행할 수 있게 함)"""
import cv2
import numpy as np


def make_sample(path="sample.jpg"):
    img = np.full((480, 640, 3), 230, dtype=np.uint8)
    cv2.rectangle(img, (60, 80), (220, 300), (60, 90, 200), -1)      # 카드 모양 1
    cv2.rectangle(img, (280, 120), (430, 330), (200, 140, 60), -1)   # 카드 모양 2
    cv2.circle(img, (520, 200), 70, (80, 180, 90), -1)               # 원
    cv2.putText(img, "OpenCV", (70, 420), cv2.FONT_HERSHEY_SIMPLEX,
                1.6, (30, 30, 30), 3)
    cv2.imwrite(path, img)
    return path
