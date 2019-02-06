import cv2
import numpy as np
import matplotlib.pyplot as plt
#Below code is for corner detection
img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
    
cv2.imshow('Corner', img)
#Below code is for feature matching

img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()

