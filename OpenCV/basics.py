import cv2

img = cv2.imread("Python/OpenCV/pictures/abqce_png.rf.67ce8ee979f106d76fdc9dbb093ac991.jpg", 1)
img2 = cv2.imread("Python/OpenCV/pictures/adrhr_png.rf.487e446b0b7f657c4a11abc311348415.jpg", 1)
img3 = cv2.imread("Python/OpenCV/pictures/agnhj_png.rf.3a6ad8649332c6c20a56b165317e6cfe.jpg", 1)

img = cv2.resize(img, (500, 500))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_180) # ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE

#cv2.imwrite('new.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


