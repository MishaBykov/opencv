import math
import cv2

color_red = (0, 0, 255)
color_green = (0, 255, 0)
color_yellow = (0, 255, 255)
color_purple = (255, 0, 255)
cap = cv2.VideoCapture("03.wmv")
template = cv2.imread("opponent.bmp")
fgbg = cv2.createBackgroundSubtractorMOG2()
i = 0
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    height, width = frame.shape[:-1]
    fgmask = fgbg.apply(frame)
    if fgmask is None:
        break
    cv2.medianBlur(fgmask, 9, fgmask)

    im2, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # Поиск контуров
    # fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    # cv2.drawContours(fgmask, contours, -1, color_red, 2, 8, hierarchy)
    point_robot = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)  # Поиск ограничивающего прямоугольника
        if w < 50:
            continue
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_purple, 2)
        # cv2.rectangle(fgmask, (x, y), (x + w, y + h), color_green, 2)
        point_robot = (x + int(w / 2), y + int(h / 2))
        cv2.circle(frame, point_robot, 3, (0, 0, 255), -1)
    w, h = template.shape[:-1]
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    cv2.normalize(result, result, 1, 0, cv2.NORM_MINMAX)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + h, top_left[1] + w)
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    point_opponent = (top_left[0] + int(h / 2), top_left[1] + int(w / 2))
    cv2.circle(frame, point_opponent, 3, (0, 0, 255), -1)
    if point_robot != 0:
        cv2.line(frame, point_robot, point_opponent, color_green, 2)
        distance = math.sqrt(math.pow(point_robot[0] - point_opponent[0], 2)
                             + math.pow(point_robot[1] - point_opponent[1], 2))
        cv2.putText(frame, str(round(distance, 3)), (0, height - 5), cv2.FONT_HERSHEY_PLAIN, 2, color_yellow, 1)
    cv2.putText(frame, str(i), (0, 25), cv2.FONT_HERSHEY_PLAIN, 2, color_yellow, 1)
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        cv2.imwrite('frame.png', frame)
        cv2.imwrite('fgmask.png', fgmask)
        break
    i += 1
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
