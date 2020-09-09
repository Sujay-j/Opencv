import cv2
import numpy as np

#img = cv2.imread('DSC.jpg',4)
img = np.zeros([512,512,3],np.uint8)

#img = cv2.line(img,(0,0),(255,255),(255,0,0),10)

#img = cv2.arrowedLine(img,(255,150),(90,90),(0,255,0),10)

img = cv2.rectangle(img,(150,30),(210,110),(0,150,150),10)
img = cv2.circle(img,(180,70),40,(0,0,255),3)
img = cv2.putText(img ,'Sujay',(10,200),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)






cv2.imshow('image',img)



cv2.waitKey(0)
cv2.destroyAllWindows()
