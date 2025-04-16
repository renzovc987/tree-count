import cv2

# Load image as greyscale
im = cv2.imread('imagen_satelital.tif', cv2.IMREAD_GRAYSCALE)

# Apply blur
blur = cv2.GaussianBlur(im,(19,19),0)

# Otsu threshold
_,thr = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Create a resizable window
cv2.namedWindow('result', cv2.WINDOW_NORMAL)

# Show the image
cv2.imshow('result', thr)
