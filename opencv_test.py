import cv2

img = cv2.imread('gpsImg.jpg', cv2.IMREAD_COLOR)
down_width = 427
down_height = 613
down_points = (down_width, down_height)
resized_down = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
cv2.imshow('image', resized_down)
cv2.waitKey(0)
cv2.destroyWindow('image')
