import cv2
import numpy as np
# create blank imagae
def cross(x):
    pass
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("color picker")
# create switch
s="0:off 1:on"
cv2.createTrackbar(s,"color picker",0,1,cross)
cv2.createTrackbar("R","color picker",0,255,cross)
cv2.createTrackbar("G","color picker",0,255,cross)
cv2.createTrackbar("B","color picker",0,255,cross)

# display imaga
while True:
    cv2.imshow("color picker",img)
    if cv2.waitKey(1)&0xff==27:
        break
# gatting the values
    switch=cv2.getTrackbarPos(s,"color picker")
    r=cv2.getTrackbarPos("R","color picker")
    g=cv2.getTrackbarPos("G","color picker")
    b=cv2.getTrackbarPos("B","color picker")

# for checking
    if switch==0:
        img[:]=0
    else:
        img[:]=[r,g,b]
cv2.destroyAllWindows()







