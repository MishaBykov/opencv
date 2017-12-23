import cv2
import numpy as np
from matplotlib import pyplot as plt


def show_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)


image = cv2.imread("test.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)  # Бинаризация
im2, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # Поиск контуров
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image, contours, -1, (0, 100, 0), 2)
show_image(image)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)  # Поиск ограничивающего прямоугольника
    # if w < 50:
    #     continue  # Маленькие контуры меньше 50 пикселей не нужны
    cv2.rectangle(image, (x, y), (x + w, y + h), (100, 0, 0), 2)
show_image(image)
