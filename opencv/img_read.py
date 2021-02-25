################## Read Image ################
# import cv2
# #Load an Image using 'imread'
# img = cv2.imread("Resources/lena.png")
# # Display
# cv2.imshow("lena",img)
# cv2.waitKey(0)


############### Read Video##################
# import cv2

# cap = cv2.VideoCapture("Resources/test_video.mp4")

# while True:
#     succes, img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


############### Read WebCam ##############
import cv2 
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,100) # brightness

while True:
    succes, img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break