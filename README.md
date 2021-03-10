# video-frame-extractor
video frame extraction from a clip for dataset creation.

```frame-generator.py``` generates all the frames from a sample video that will be saved into ```extracted-frames``` directory.

## Installation of Packages :

we will need ```opencv``` and ```os``` package of python for this project. from python3.4 onwards, os is an integral part of python. We will need to install opencv for running the ```frame-generator.py```. It is advised that you use virtual environment for any vision related project to avoid conflict of package dependency.

```commandline
pip3 install opencv-python
```
## Running the code :
- keep the video clip and the python file under same directory
- rename the video clip as 'sample-input.mp4', if you don't want to change the code
- hit ```python3 frame-generator.py``` in commandline. you should see the frames of your video clips extracted into extracted-frames directory.

## Acknowledgement :
In the process of writing this frame-generator.py code the following links helped a lot. You can check them out.
- [thispointer](https://thispointer.com/how-to-create-a-directory-in-python/)
- [stackoverflow](https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames)