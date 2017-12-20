import numpy as np
import cv2

cap = cv2.VideoCapture("03.wmv")
fgbg = cv2.createBackgroundSubtractorMOG2()
while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.medianBlur(fgmask, 9, fgmask)
    moments = cv2.moments(fgmask, 1)  # получим моменты
    y_moment = moments['m01']
    x_moment = moments['m10']
    area = moments['m00']
    if area != 0:
        x = int(x_moment / area)  # Получим координаты x,y кота
        y = int(y_moment / area)  # и выведем текст на изображение
        cv2.putText(frame, "Cat!", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
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
