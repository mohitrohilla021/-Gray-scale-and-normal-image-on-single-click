import numpy as np
import cv2

def callback_fn(x):
    print(x)

# let's create a empty black image...
#img = np.zeros((300,512,3),np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('curr_pos','image',10,400,callback_fn)
switch = 'color/gray'
cv2.createTrackbar(switch,'image',0,1,callback_fn)

while True:
    img = cv2.imread('one.jpg')
    pos = cv2.getTrackbarPos('curr_pos', 'image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(0,0,255),8)
    k = cv2.waitKey(1)&0xff
    if k == ord('q'):
        break
    s = cv2.getTrackbarPos(switch,'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('image',img)
cv2.destroyAllWindows()
