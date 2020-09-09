import numpy as np
import cv2
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt 

kernal = np.ones((5,5),np.float32)/25
img = cv2.imread('DSC.jpg')
#img1 = cv2.imread('smarites.png',cv2.IMREAD_GRAYSCALE)
#img = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2RGB)

dat = cv2.filter2D(img,-1,kernal)
blur = cv2.blur(img,(5,5))
gausianblur=cv2.GaussianBlur(img,(5,5),0)
medianblur=cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)




titles=['image']
images=[img]

#for i in range(3):
#    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

cv2.imshow('frame',img)
cv2.imshow('frame1',dat)
cv2.imshow('frame2',blur)
cv2.imshow('frame3',gausianblur)
cv2.imshow('frame4',medianblur)
cv2.imshow('frame5',bilateral)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
