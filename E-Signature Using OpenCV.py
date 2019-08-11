import numpy as np
import cv2

frame=np.ones([800,800,3],'uint8')*255
radius=10

color=(255,0,0)
pressed=False


def draw_signature(event,x,y,param,flags):
        global pressed
        ix,iy=x,y
        if event==cv2.EVENT_LBUTTONDOWN:
                cv2.line(frame,(ix,iy),(x,y),color,10)
                pressed=True
        elif event==cv2.EVENT_MOUSEMOVE and pressed==True:
                cv2.line(frame,(ix,iy),(x,y),color,10)
        elif event==cv2.EVENT_LBUTTONUP:
                pressed=False
                

cv2.namedWindow("frame")
cv2.setMouseCallback("frame",draw_signature)
        
        


while(True):
        cv2.imshow("frame",frame)
        ch=cv2.waitKey(1)
        if ch&0xFF==ord('q'):
                break
        elif ch&0xFF==ord('g'):
                color=(0,255,0)
        elif ch&0xFF==ord('r'):
                color=(0,0,255)
        
cv2.destroyAllWindows()

