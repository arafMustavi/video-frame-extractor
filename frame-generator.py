import cv2
import os

dirName = 'extracted-frames'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

vidcap = cv2.VideoCapture('sample-input.mp4')

success,image = vidcap.read()   
frame_count = 0

while success:
    cv2.imwrite('extracted-frames/frame{}.jpg'.format(frame_count), image)     
    success,image = vidcap.read()
    print('Read a new frame:', success,'Next Frame Number: {}'.format(frame_count))
    frame_count += 1