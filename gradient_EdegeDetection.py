import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt 

kernal = np.ones((5,5),np.float32)/25
img = cv2.imread('sudoku.jpg',cv2.IMREAD_GRAYSCALE)
lap =cv2.Laplacian(img,cv2.CV_64F , ksize = 1)#64f is float to supprt negative numbers
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelx = np.uint8(np.absolute(sobelx))

sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobely = np.uint8(np.absolute(sobely))

sobelCombine = cv2.bitwise_or(sobelx,sobely)

canny = cv2.Canny(img,100,200)


titles=['image']
images=[img]

#for i in range(3):
#    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()

cv2.imshow('frame',img)
cv2.imshow('frame1',lap)
cv2.imshow('frame2',sobelx)
cv2.imshow('frame3',sobely)
cv2.imshow('frame4',sobelCombine)
cv2.imshow('frame5',canny)





cv2.waitKey(0)   
cv2.destroyAllWindows()
#cap.release()
