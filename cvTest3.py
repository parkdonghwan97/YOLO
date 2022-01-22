import cv2 as cv

# cap = cv.VideoCapture('video/z.mp4')
cap = cv.VideoCapture(cv.CAP_DSHOW) # cap = cv.VideoCapture(0) # 웹캠이뜸;
while True:
    retval , frame = cap.read()
    if not retval :
        print('캡처 실패')
        break
    else:
        cv.imshow('video', frame)
        key = cv.waitKey(1)
        if key ==27 :   # esc 번호가 27임  esc 누르면 종료
            break
cap.release()
cv.destroyAllWindows()