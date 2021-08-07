# 人脸检测与眼睛检测试验
import cv2
import matplotlib.pyplot as plt
# openCV中的检测器路径
print(cv2.__file__)

img = cv2.imread('004.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 实例化检测器
face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cas.load("haarcascade_frontalface_default.xml")

eyes_cas = cv2.CascadeClassifier("haarcascade_eye.xml")
eyes_cas.load("haarcascade_eye.xml")

# 人脸检测
face_rects = face_cas.detectMultiScale(gray) # 使用默认参数，否则, scaleFactor=1.2, minNeighbors=3, maxSize=(32, 32)无效果
# 绘制人脸并眼睛检测
for facerect in face_rects:
    x, y, w, h = facerect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 3)
plt.imshow(img[:, :, ::-1])
plt.show()