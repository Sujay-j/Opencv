import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('gradientt.png')
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=['original','binary','binary_inv','trunc','tozero','tozero_inv']
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks()
    
plt.show()

#cv2.imshow("image",img) 
#cv2.imshow("image1",th1) 
#cv2.imshow("image3",th3)
#cv2.imshow("image2",th2) 
#cv2.imshow("image4",th4)
#cv2.imshow("image5",th5) 

cv2.waitKey(0)
   
cv2.destroyAllWindows()
#cap.release()