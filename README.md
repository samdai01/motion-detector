# Camera Motion Detector and Face Recognition Program
This program takes an input feed and detects new objects that enter the field of vision of the camera. Implemented in python with the use of the OpenCV libaray for motion detection, video highlighting, and object highlights. 

# Process
This program first takes the first input frame from the video and sets it as the background. It will then proceed to compare each subsequent frame with this original background frame and highlight the differences. ![image](https://user-images.githubusercontent.com/89489298/149049540-697bc27c-95ff-4483-ae13-4f9b52146137.png)



The program takes each frame of the input feed from the camera and converts it to a grayscale image ![image](https://user-images.githubusercontent.com/89489298/149049273-dad07f27-fb1c-4472-b463-dc95a60a69aa.png)
, then a black and white image that is composed of the differences between the first frame and the current frame ![image](https://user-images.githubusercontent.com/89489298/149049365-e5afdeb8-86f8-44b6-9d4e-18d0918b596b.png)
. These differences are highlighted in white ![image](https://user-images.githubusercontent.com/89489298/149049388-09f9c74f-dbf8-49e7-89ed-3ac47299e7a0.png)
. The program then proceeds to take the coordinates of these differences and box them at the correct location over the original color feed. 

# Setup and Installation Requirements:
First you will need to install the OpenCV library using the command `pip3.9 install opencv-python`. If there is still an error in the code on the `import cv2` line, run the command `pip3.9 uninstall opencv-python` and then `pip3.9 install opencv-python opencv-python-headless`. 

You will also have to install the pandas library and bokeh libraries if not done so. When running the program, make sure the program starts with the background with no objects in it (explained below). Make sure that you are running `plotting.py` and `capture_video.py` is in the same folder. 


