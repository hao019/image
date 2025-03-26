import cv2
import numpy as np

def resize_image(image, scale, interpolation):
    height, width = image.shape[:2]
    new_size = (int(width * scale), int(height * scale))
    return cv2.resize(image, new_size, interpolation=interpolation)

def main():
    # 讀取影像
    image = cv2.imread('image.jpg')  # 請確保影像檔案 'image.jpg' 存在
    
    if image is None:
        print("無法讀取影像，請檢查檔案路徑！")
        return
    
    # 影像縮放 (使用不同插值法)
    scale_factor = 2.0  # 縮放比例
    resized_nearest = resize_image(image, scale_factor, cv2.INTER_NEAREST)
    resized_linear = resize_image(image, scale_factor, cv2.INTER_LINEAR)
    resized_cubic = resize_image(image, scale_factor, cv2.INTER_CUBIC)
    resized_lanczos = resize_image(image, scale_factor, cv2.INTER_LANCZOS4)
    
    # 顯示原始影像
    cv2.imshow('Original Image', image)
    
    # 顯示縮放後的影像
    cv2.imshow('Resized - Nearest', resized_nearest)
    cv2.imshow('Resized - Linear', resized_linear)
    cv2.imshow('Resized - Cubic', resized_cubic)
    cv2.imshow('Resized - Lanczos', resized_lanczos)
    
    # 等待按鍵按下再關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
