# -*- encoding: UTF-8 -*-
# 创建一个色域选择器
import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
img = cv2.imread('003.png')
img = cv2.resize(img, (640, 240))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('img', img)
cv2.imshow('imgHSV', imgHSV)
cv2.createTrackbar('h_min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('h_max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('s_min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('s_max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('v_min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('v_max', 'TrackBars', 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos("h_min", 'TrackBars')
    h_max = cv2.getTrackbarPos("h_min", 'TrackBars')
    s_min = cv2.getTrackbarPos("s_min", 'TrackBars')
    s_max = cv2.getTrackbarPos("s_max", 'TrackBars')
    v_min = cv2.getTrackbarPos("v_min", 'TrackBars')
    v_max = cv2.getTrackbarPos("v_max", 'TrackBars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('mask', mask)
    cv2.imshow('Result', imgResult)
    k = cv2.waitKey(100) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()