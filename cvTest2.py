import cv2 as cv

# img = cv.imread('street_view.jpg',cv.IMREAD_COLOR)
# img = cv.imread('street_view.jpg',cv.IMREAD_GRAYSCALE)
img = cv.imread('street_view.jpg',cv.IMREAD_UNCHANGED)
# False: 0, None, [], (), {} , ''
# True:0이아닌 정수또는 실수, 'abc', (10,20),[10],{'a':10},객체생성
if img is None: # if not img
    print( '이미지를 읽을 없습니다.')
    exit(1)
print( type(img), img.shape )
print( img )
cv.imshow('street', img) # ctrl + q
#key = cv.waitKey(0) #hold
key = cv.waitKey(2000) #hold
print( "key", key )
cv.destroyAllWindows()