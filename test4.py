import cv2
import numpy as np

def resize_image(image, scale, interpolation):
    height, width = image.shape[:2]
    new_size = (int(width * scale), int(height * scale))
    return cv2.resize(image, new_size, interpolation=interpolation)

def detect_and_crop_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        print("未偵測到人臉")
        return None
    
    x, y, w, h = faces[0]  # 取第一個偵測到的人臉
    face_image = image[y:y+h, x:x+w]
    return face_image

def main():
    # 讀取影像
    image = cv2.imread('image2.jpg')  # 請確保影像檔案 'image.jpg' 存在
    
    if image is None:
        print("無法讀取影像，請檢查檔案路徑！")
        return
    
    # 人臉裁切
    face_image = detect_and_crop_face(image)
    
    if face_image is not None:
        # 顯示原始影像
        cv2.imshow('Original Image', image)
        cv2.imshow('Cropped Face', face_image)
    
    # 等待按鍵按下再關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()