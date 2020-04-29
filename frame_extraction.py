# Importing all necessary libraries 
import cv2 
import os   

#**************************************************************************************
import numpy as np
import cv2
cap = cv2.VideoCapture('video.mp4') #video_name is the video being called  , video.webm girl.mp4
# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frame per seconds:",fps)
# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print("Frame count: ",int(frame_count))

frame_no=359
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

ret, frame = cap.read() # Read the frame
#cv2.imshow('frame0', frame) # show frame on window
cv2.imwrite('user_frame_is.jpg', frame)
#cv2.waitKey(1000)
cv2.destroyAllWindows()
#************************************************************************************** 


'''frame_no=25
#cap.set(444,frame_no); # Where frame_no is the frame you want
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
ret, frame = cap.read() # Read the frame
#cv2.imshow('frame_is', frame) # show frame on window
cv2.imwrite('frame_is.jpg', frame)'''




'''import numpy as np
import cv2

#Get video name from user
#Ginen video name must be in quotes, e.g. "pirkagia.avi" or "plaque.avi"
#video_name = input("Please give the video name including its extension. E.g. \"pirkagia.avi\":\n")
video_name='girl.mp4'  #video.webm
#Open the video file
cap = cv2.VideoCapture(video_name)

#Set frame_no in range 0.0-1.0
#In this example we have a video of 30 seconds having 25 frames per seconds, thus we have 750 frames.
#The examined frame must get a value from 0 to 749.
#For more info about the video flags see here: https://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python
#Here we select the last frame as frame sequence=749. In case you want to select other frame change value 749.
#BE CAREFUL! Each video has different time length and frame rate. 
#So make sure that you have the right parameters for the right video!
time_length = 11
fps=24.0
frame_seq = 264
frame_no = (frame_seq /(time_length*fps))

#The first argument of cap.set(), number 2 defines that parameter for setting the frame selection.
#Number 2 defines flag CV_CAP_PROP_POS_FRAMES which is a 0-based index of the frame to be decoded/captured next.
#The second argument defines the frame number in range 0.0-1.0
cap.set(200,frame_no);

#Read the next frame from the video. If you set frame 749 above then the code will return the last frame.
ret, frame = cap.read()

#Set grayscale colorspace for the frame. 
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Cut the video extension to have the name of the video
my_video_name = video_name.split(".")[0]

#Display the resulting frame
cv2.imshow(my_video_name+' frame '+ str(frame_seq),gray)

#Set waitKey 
cv2.waitKey()

#Store this frame to an image
cv2.imwrite(my_video_name+'_frame_'+str(frame_seq)+'.jpg',gray)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()'''
