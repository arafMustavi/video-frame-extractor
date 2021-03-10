# video-frame-extractor
video frame extraction from a clip for dataset creation.

`frame-generator.py` generates all the frames from a sample video that will be saved into ```extracted-frames``` directory.

## Dependency and Installation of Packages :

we will need `opencv` and `os` package of python for this project. from python3.4 onwards, os is an integral part of python. We will need to install opencv for running the `frame-generator.py`. It is advised that you use virtual environment for any computer-vision related project to avoid conflict of package dependency.

```commandline
pip3 install opencv-python
```
## Running the code :
- create a directory with the name `dataset-sample` . 
- keep the video clips in the newly created `dataset-sample` directory . 
- make sure that `frame-generator.py` and `dataset-sample` directory are kept under same directory .
- hit `python3 frame-generator.py` in commandline. 
- you should see the frames of your video clips extracted into `extracted-frames` directory.

## Acknowledgement :
In the process of writing this frame-generator.py code the following links helped a lot. You can check them out.
- [thispointer](https://thispointer.com/how-to-create-a-directory-in-python/)
- [stackoverflow](https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames)
