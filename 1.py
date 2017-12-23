import cv2

source = cv2.imread("1.bmp")

template = cv2.imread("opponent.bmp")
w, h = template.shape[:-1]
result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
cv2.normalize(result, result, 1, 0, cv2.NORM_MINMAX)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + h, top_left[1] + w)

cv2.rectangle(source, top_left, bottom_right, 255, 2)
cv2.imshow('Result', source)
cv2.waitKey(0)
