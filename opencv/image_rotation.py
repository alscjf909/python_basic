import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250,350
print("width : {0}  Height :{1} ".format(width,height))
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) 
pts2 = np.float32([[0,0], [width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
print(matrix)
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)

# import numpy as np
# import cv2


# point_list = []
# count = 0
# width, height = 250,350
# def mouse_callback(event, x, y, flags, param):
#     global point_list, count, img_original


#     # 마우스 왼쪽 버튼 누를 때마다 좌표를 리스트에 저장
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("(%d, %d)" % (x, y))
#         point_list.append((x, y))

#         print(point_list)
#         cv2.circle(img_original, (x, y), 3, (0, 0, 255), -1)



# cv2.namedWindow('original')
# cv2.setMouseCallback('original', mouse_callback)

# # 원본 이미지
# img_original = cv2.imread('Resources/cards.jpg')


# while(True):

#     cv2.imshow("original", img_original)


#     if cv2.waitKey(1)&0xFF == 32: # spacebar를 누르면 루프에서 빠져나옵니다.
#         break


# # 좌표 순서 - 상단왼쪽 끝, 상단오른쪽 끝, 하단왼쪽 끝, 하단오른쪽 끝
# pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2]),list(point_list[3])])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# print(pts1)
# print(pts2)

# M = cv2.getPerspectiveTransform(pts1,pts2)

# img_result = cv2.warpPerspective(img_original, M, (width,height))


# cv2.imshow("result1", img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()