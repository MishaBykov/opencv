import cv2

color_red = (0, 0, 255)
color_yellow = (0, 255, 255)
color_purple = (255, 0, 255)

img = cv2.imread('1.bmp')
height, width = img.shape[:-1]
# рисуем окружность
cv2.circle(img, (190, 70), 2, color_red, -1)
# рисуем прямоугольник
cv2.rectangle(img, (180, 140), (370, 180), color_red, thickness=2, lineType=8, shift=0)
# рисуем пять отрезков
for i in range(5):
    cv2.line(img, (180, 85 + i * 5), (370, 85 + i * 5), color_purple, thickness=2, lineType=8, shift=0)
# выводим текст
cv2.putText(img, "Hello world!", (0, height-5), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)

cv2.imshow('result', img)

ch = cv2.waitKey()

cv2.destroyAllWindows()
