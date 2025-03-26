import cv2
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    # 計算旋轉矩陣
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # 進行旋轉
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

def main():
    # 讀取影像
    image = cv2.imread('image.jpg')  # 請確保影像檔案 'image.jpg' 存在
    
    if image is None:
        print("無法讀取影像，請檢查檔案路徑！")
        return
    
    # 旋轉影像
    rotated_15 = rotate_image(image, 15)
    rotated_neg30 = rotate_image(image, -30)
    
    # 顯示原始影像
    cv2.imshow('Original Image', image)
    
    # 顯示旋轉後的影像
    cv2.imshow('Rotated 15 Degrees', rotated_15)
    cv2.imshow('Rotated -30 Degrees', rotated_neg30)
    
    # 等待按鍵按下再關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
