import cv2 as cv

img = cv.imread('street_view.jpg')

if img is None:
    print("이미지 못읽음")
    exit(1)
print(img)
cv.imshow('street',img)

key = cv.waitKey(0)
print('key',key)
cv.destroyAllWindows()



img = cv.imread('street_view.jpg',cv.IMREAD_GRAYSCALE)
if img is None:
    print("이미지 못읽음")
    exit(1)
print(img)
cv.imshow('street',img)
key=cv.waitKey(2000)

print('key',key)
cv.destroyAllWindows()

cap = cv.VideoCapture('video/z.mp4')
while True:
    retval , frame = cap.read()
    if not retval :
        print('캡처 실패')
        break
    else:
        cv.imshow('video', frame)
        key = cv.waitKey(100)
        if key ==27 :   # esc 번호가 27임  esc 누르면 종료
            break
cap.release()
cv.destroyAllWindows()

cap = cv.VideoCapture('video/z.mp4')
if cap.isOpened() ==False:
    print("웹캠이 없다.")
    exit(1)

ret, image = cap.read() # return , image
print(image.shape)
h ,w = image.shape[:-1]    # (480, 640)
fps = 30  # 초당 30개 이미지 저장
# codec = cv.VideoWriter_fourcc(*'MJPV')   # avi 코덱
codec = cv.VideoWriter_fourcc(*'mp4v')   # mp4 코덱
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