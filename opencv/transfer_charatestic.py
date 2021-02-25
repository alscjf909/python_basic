
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
print(kernel)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ## color change
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)  # 항상 (n,n) n홀수 여야됨
imgCanny = cv2.Canny(img,150,200) #  edge를 나타냄 (img, x, y) 값을 올리면 edge가 더 뚜렸하게 나타남
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #이미지 형태 전환 팽창 - dilation
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erosion Image", imgEroded)
cv2.waitKey(0)