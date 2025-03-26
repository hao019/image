import cv2

def main():
    # 讀取影像
    image = cv2.imread('image.jpg')  # 請確保影像檔案 'image.jpg' 存在
    
    if image is None:
        print("無法讀取影像，請檢查檔案路徑！")
        return
    
    # 顯示影像
    cv2.imshow('Display Image', image)
    
    # 等待按鍵按下再關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
