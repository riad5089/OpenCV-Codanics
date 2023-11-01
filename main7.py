#converting video to gray or  black and white
import cv2 as cv

cap = cv.VideoCapture('resources/pexels_videos_2099568 (1080p).mp4')


# reading and playing
while True:
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #gray color image
    (thresh, b_w) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)  # binary black and white

    if ret==True:
        resized_frame = cv.resize(b_w, (800, 800))
        #resized_frame = cv.resize(grayframe, (800, 800))
        cv.imshow("Video",resized_frame)
        if cv.waitKey(1) & 0xFF==ord('q'): #0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
