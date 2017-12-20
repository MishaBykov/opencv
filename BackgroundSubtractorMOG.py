import cv2

cap = cv2.VideoCapture('03.wmv')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.medianBlur(fgmask, 5, fgmask)
    if fgmask is None:
        break
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
