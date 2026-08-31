"""
[활용편6 21] 얼굴 검출 + 캐릭터(스티커) 씌우기
- Face Detection(얼굴 검출) : 얼굴이 '어디에' 있는지 위치만 반환
- Face Recognition(얼굴 인식) : '누구인지'까지 구별
  → 이 과제는 누구인지가 중요하지 않으므로 얼굴 검출이 적합하다.

코드 흐름 : 웹캠 프레임 읽기 → 좌우 반전 → BGR→RGB 변환
            → MediaPipe 얼굴 검출 → 눈·코 특징점 좌표 계산
            → 스티커 합성 → 화면 출력

알파 블렌딩 : 결과 = 스티커색 x 알파 + 배경색 x (1 - 알파)
              알파가 1이면 스티커만, 0이면 배경만 보인다.
"""
import cv2
import numpy as np
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection


def overlay(image, x, y, w, h, overlay_image):
    """투명 PNG(4채널)를 image 위에 자연스럽게 합성"""
    x1, y1 = x - w, y - h
    x2, y2 = x + w, y + h
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]:
        return                                   # 화면 밖으로 나가면 건너뜀

    part = overlay_image[:, :, :]
    alpha = part[:, :, 3:4].astype(float) / 255.0   # 0.0 ~ 1.0 마스크
    roi = image[y1:y2, x1:x2]
    image[y1:y2, x1:x2] = (part[:, :, :3] * alpha + roi * (1 - alpha)).astype(np.uint8)


def main():
    cap = cv2.VideoCapture(0)

    # 스티커 이미지(투명 PNG). 없으면 원으로 대체
    right_eye = cv2.imread("right_eye.png", cv2.IMREAD_UNCHANGED)
    left_eye = cv2.imread("left_eye.png", cv2.IMREAD_UNCHANGED)

    with mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.7) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break

            image = cv2.flip(image, 1)                        # 좌우 반전(거울 모드)
            image.flags.writeable = False
            results = face_detection.process(
                cv2.cvtColor(image, cv2.COLOR_BGR2RGB))       # BGR → RGB
            image.flags.writeable = True

            if results.detections:
                for detection in results.detections:
                    keypoints = detection.location_data.relative_keypoints
                    h, w, _ = image.shape
                    # 0: 오른쪽 눈, 1: 왼쪽 눈, 2: 코끝
                    re = (int(keypoints[0].x * w), int(keypoints[0].y * h))
                    le = (int(keypoints[1].x * w), int(keypoints[1].y * h))

                    if right_eye is not None and left_eye is not None:
                        overlay(image, *re, 50, 50, right_eye)
                        overlay(image, *le, 50, 50, left_eye)
                    else:
                        cv2.circle(image, re, 30, (255, 0, 0), -1, cv2.LINE_AA)
                        cv2.circle(image, le, 30, (0, 255, 0), -1, cv2.LINE_AA)

            cv2.imshow("Face Detection", image)
            if cv2.waitKey(1) == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
