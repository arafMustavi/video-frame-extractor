import cv2
import os

# load all the videos in the sample-clips
video_clip_list = os.listdir('./sample-clips')
print('Total {} videos are found in the sample-clips directory'.format(len(video_clip_list)))

# create a directory for the extracted frames
dirName = 'extracted-frames'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")


# extract frames from a video by processing one video at a time
for sample_clip in video_clip_list:
    video_path = 'sample-clips/' + str(sample_clip)    
    vidcap = cv2.VideoCapture(video_path)
# get frames-per-second information
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print ("Frames per second for {} is : {}".format(sample_clip,int(fps)))
  
    success,image = vidcap.read()   
    frame_count = 0
    while success:
        cv2.imwrite('extracted-frames/{}-frame{}.jpg'.format(sample_clip,frame_count), image)     
        success,image = vidcap.read()
        frame_count += 1
    print('Total {} frames has been extracted from {}\n'.format(frame_count,sample_clip))
    vidcap.release()
