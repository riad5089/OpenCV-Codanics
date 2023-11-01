#writting videos from cam
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
#writing format,codec,video writer object and file output
out=cv.VideoWriter("resources/cam_myvideo.avi",cv.VideoWriter_fourcc("M","J","p","G"),10, (frame_width,frame_height))
# ocut=cv.VideoWriter("resources/Out_video.mp4",cv.VideoWriter_fourcc(*"mp4v"),10, (frame_width,frame_height))

# reading and playing
while True:
    (ret,frame)=cap.read()
    # (thresh, b_w) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)  # binary black and white

    if ret==True:
        resized_frame = cv.resize(frame, (800, 800))
        out.write(resized_frame)
        #resized_frame = cv.resize(grayframe, (800, 800))
        cv.imshow("Video",resized_frame)
        if cv.waitKey(1) & 0xFF==ord('q'): #0 means not stopable #if i do 1 video will run 0xFF==ord('q') stoping condition
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()

