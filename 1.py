import cv2

cascadePath = r"c:\OpenCV2.2\data\haarcascades\haarcascade_frontalface_default.xml"
cascade = cv2.Load(cascadePath)
memstorage = cv.CreateMemStorage()
capture = cv.CaptureFromCAM(0)
outimage = None
name = 'window'
cv.NamedWindow(name)
while True:
    frame = cv.QueryFrame(capture)
    key = cv.WaitKey(10)
    if key != -1:
        break
    if not frame:
        break
    if outimage is None or cv.GetSize(frame) != cv.GetSize(outimage):
        outimage = cv.CreateImage(cv.GetSize(frame), 8, 3)
    cv.Flip(frame, outimage, 1)
    faces = cv.HaarDetectObjects(outimage, cascade, memstorage)
    for rect, n in faces:
        cv.Rectangle(outimage, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0) )
    cv.ShowImage(name, outimage)