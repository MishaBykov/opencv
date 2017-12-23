import numpy as np
import cv2


def moments(fgmask, frame):
    moments = cv2.moments(fgmask, 1)  # получим моменты
    y_moment = moments['m01']
    x_moment = moments['m10']
    area = moments['m00']
    if area != 0:
        x = int(x_moment / area)  # Получим координаты x,y кота
        y = int(y_moment / area)  # и выведем текст на изображение
        cv2.putText(frame, "Cat!", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cap = cv2.VideoCapture("03.wmv")
fgbg = cv2.createBackgroundSubtractorMOG2()
while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.medianBlur(fgmask, 9, fgmask)
    # moments(fgmask, frame)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)  # Бинаризация
    im2, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # Поиск контуров
    cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(fgmask, contours, -1, (0, 100, 0), 2)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)  # Поиск ограничивающего прямоугольника
        if w < 50:
            continue  # Маленькие контуры меньше 50 пикселей не нужны
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 0, 0), 2)

    if fgmask is None:
        break
    else:
        cv2.imshow('frame1', fgmask)
        cv2.imshow('frame2', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

# CvMemStorage * storage = cvCreateMemStorage(0);
#
# CvSeq * contours = 0;
# cvFindContours(gray, storage, & contours, sizeof(CvContour),
# CV_RETR_TREE, CV_CHAIN_APPROX_NONE, cvPoint(0, 0) ); // Поиск
# контуров
#
# for (CvSeq * c=contours; c != NULL; c=c->h_next)
# {
#     CvRect
# Rect = cvBoundingRect(c); // Поиск
# ограничивающего
# прямоугольника
# if (Rect.width < 50)
# continue; // Маленькие
# контуры
# меньше
# 50
# пикселей
# не
# нужны
#
# cvRectangle(image, cvPoint(Rect.x, Rect.y), cvPoint(Rect.x + Rect.width, Rect.y + Rect.height), CV_RGB(255, 0, 0), 2);
# }
#
# cvReleaseMemStorage( & storage);
#
# cvSaveImage("image24.png", image);
