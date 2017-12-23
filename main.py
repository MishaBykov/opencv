import numpy as np
import cv2

cap = cv2.VideoCapture("03.wmv")
template = cv2.imread("opponent.bmp")
fgbg = cv2.createBackgroundSubtractorMOG2()
while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    if fgmask is None:
        break
    cv2.medianBlur(fgmask, 9, fgmask)

    im2, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # Поиск контуров
    cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(fgmask, contours, -1, (0, 100, 0), 2)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)  # Поиск ограничивающего прямоугольника
        if w < 50:
            continue  # Маленькие контуры меньше 50 пикселей не нужны
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 0, 0), 2)

    w, h = template.shape[:-1]
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    cv2.normalize(result, result, 1, 0, cv2.NORM_MINMAX)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + h, top_left[1] + w)
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)

    cv2.imshow('MOG2', fgmask)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(10) & 0xff
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
