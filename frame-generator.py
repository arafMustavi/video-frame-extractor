import cv2

vidcap = cv2.VideoCapture('sample-input.mp4')
success,image = vidcap.read()
frame_count = 0

while success:
    # path = 'extracted/' + str(frame_count) + '.jpg'
    path = 'Path/Image.jpg'
    # cv2.imwrite("frame{}.jpg".format(frame_count), image)     # save frame as JPEG file      
    cv2.imwrite(path, image)     # save frame as JPEG file      

    success,image = vidcap.read()
    print('Read a new frame:', success,'Next Frame Number: {}'.format(frame_count))
    frame_count += 1