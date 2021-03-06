import cv2 
import numpy as np
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150) # brightness

myColors = [[110,30,30,130,255,255],[0,120,70,10,255,255],[25,52,72,102,255,255]
]
myColorValues = [[255,0,0],[0,17,255],[0,255,0]]
myPoints = []#[x,y,colorId]
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints


def getContours(img): # 윤곽띠
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>15000: # area 높여서 다른 바탕이 못잡게 해버리자!
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt, True) #호 길이 보여줌
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) #호의 길이를 측정하기 위해 찍힌 점)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y ## 볼펜 위에 끝에 찍기 위해서 

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0],point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img=cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0: #new point가 존재하는지 안하는지 파악 안하면 error남
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)


    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break