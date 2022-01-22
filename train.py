import cv2 as cv

cap = cv.VideoCapture('video/z.mp4')
# cap = cv.VideoCapture(cv.CAP_DSHOW) # cap = cv.VideoCapture(0) # 웹캠이뜸;
if cap.isOpened() ==False:
    print("웹캠이 없다.")
    exit(1)

ret, image = cap.read()
print(image.shape)
h ,w = image.shape[:-1]    # (480, 640)
fps = 30  # 초당 30개 이미지 저장
# codec = cv.VideoWriter_fourcc(*'MJPV')   # avi 코덱
codec = cv.VideoWriter_fourcc(*'mp4v')   # mp4 코덱
# codec = cv.VideoWriter_fourcc('M','J','P',"G")   # mp4 코덱
writer = cv.VideoWriter('video/cap.mp4',codec,fps, (w,h))   #  폭 높이 저장할 때는 반대로 해야함!  w , h
while True:
    retval , frame = cap.read()
    if not retval :
        print('캡처 실패')
        break
    else:
        writer.write(frame)
        cv.imshow('video', frame)
        key = cv.waitKey(1)
        if key == 27 :   # esc 번호가 27임  esc 누르면 종료
            break
cap.release()
writer.release()
cv.destroyAllWindows()