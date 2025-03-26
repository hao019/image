import cv2
import numpy as np

def adjust_brightness_contrast(image, alpha=1.5, beta=50):
    # alpha: 對比度增強倍率, beta: 亮度調整值
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

def resize_image(image, scale):
    height, width = image.shape[:2]
    new_size = (int(width * scale), int(height * scale))
    return cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)

def main():
    # 讀取影像
    image = cv2.imread('image.jpg')  # 請確保影像檔案 'image.jpg' 存在
    
    if image is None:
        print("無法讀取影像，請檢查檔案路徑！")
        return
    
    # 影像放大 2 倍
    resized_image = resize_image(image, 2.0)
    
    # 調整亮度與對比度
    adjusted_image = adjust_brightness_contrast(resized_image)
    
    # 顯示原始影像
    cv2.imshow('Original Image', image)
    
    # 顯示處理後影像
    cv2.imshow('Resized & Adjusted Image', adjusted_image)
    
    # 等待按鍵按下再關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
