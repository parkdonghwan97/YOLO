import cv2 as cv
import numpy as np
# https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html#line
w = 640
h = 480
arr = np.zeros((h, w, 3))    # 480, 640, 3
print(arr)
arr.fill(255)
# cv.imshow('draw', arr)  # 모두 0으로 채웠기 때문에 검정색  255로 채우면 흰색


# 사각형 그리기 cv2.rectangle(img, start, end, color, thickness)
# cv.rectangle(arr, (50, 50), (100,100) , (0,0,244),3)  # color : RBG가 아님   BGR 순임
cv.rectangle(arr, (50, 50), (100,100) , (0,0,244),-1) # 도형 안을 모두 채우기  -1

# 원 그리기 cv2.circle(img, center, radian, color, thickness)
cv.circle(arr, (w//2, h//2), 50, (255, 0, 0),3  )

# line 그리기  cv2.line(img, start, end, color, thickness)
cv.line(arr, (0,0),(200,200),(0,255,0),3   )

#Polygon 그리기 cv2.polylines(img, pts, isClosed, color, thickness) # 이미지에 표현하기 위해 3차원 행렬로 변환. 변환이전과 이후의 행렬 갯수는 동일해야함.
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32) # 각 꼭지점은 2차원 행렬로 선언 x,y 4개의 점 잇는 선
pts = pts.reshape((-1, 1, 2))
cv.polylines(arr,[pts] , True,(0,0,0) ,3  )

#  이미지에 Text 추가 cv2.putText(img, text, org, font, fontSacle, color)
cv.putText(arr, 'OpenCV',(10,400) ,cv.FONT_HERSHEY_SIMPLEX,4,(0,0,0),2) # 'OpenCV' 좌측하단의 위치가 (10,400)
cv.putText(arr, 'hello',(200,100) ,cv.FONT_HERSHEY_COMPLEX,3.5,(0,0,0),2)


# 그림 출력
cv.imshow('zz', arr)


cv.waitKey(0)
cv.destroyAllWindows()