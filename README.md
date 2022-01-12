# Camera Motion Detector and Face Recognition Program
This program takes an input feed and detects new objects that enter the field of vision of the camera. Implemented in python with the use of the OpenCV libaray for motion detection, video highlighting, and object highlights. 

# Process
This program first takes the first input frame from the video and sets it as the background. It will then proceed to compare each subsequent frame with this original background frame and highlight the differences.

The program takes each frame of the input feed from the camera and converts it to a grayscale image, then a black and white image that is composed of the differences between the first frame and the current frame. These differences are highlighted in white. The program then proceeds to take the coordinates of these differences and box them at the correct location over the original color feed. 

# Setup and Installation Requirements:
First you will need to install the OpenCV library using the command "pip3.9 install opencv-python". If there is still an error in the code on the "import cv2" line, run the command "pip3.9 uninstall opencv-python" and then "pip3.9 install opencv-python opencv-python-headless". 

You will also have to install the pandas library and bokeh libraries if not done so. When running the program, make sure the program starts with the background with no objects in it (explained below). Make sure that you are running 'plotting.py' and 'capture_video.py' is in the same folder. 


