import numpy as np
import cv2
img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150, 150), (255,255,255), 15)
cv2.rectangle(img, (15,30), (200, 175), (0,0,255), 10)
cv2.circle(img, (500, 500), 50, (0,255,0), -1)
pts = np.array([[10,50], [20,30], [35,45], [50,10]], np.int32)
#pts = pts.reshape(-1, 1, 2)
cv2.polylines(img, [pts], True, (0,255,255), 5)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'MY Drawing!', (0, 600), font, 1, (200, 198, 187), 5, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()