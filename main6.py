import cv2 as  cv
cap=cv.VideoCapture('resources/pexels_videos_2099568 (1080p).mp4')
#indecator
if (cap.isOpened()==False):
    print("error in reading video")

#reading and playing
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        resized_frame = cv.resize(frame, (800, 800))
        cv.imshow("Video",resized_frame)
        if cv.waitKey(1) & 0xFF==ord('q'): #0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()
