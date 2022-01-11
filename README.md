# Camera Motion Detector and Face Recognition Program
This program takes an input feed and detects new objects that enter the field of vision of the camera. Implemented in python with the use of the OpenCV libaray for motion detection, video highlighting, and object highlights. 

# Process
The program takes each frame of the input feed from the camera and converts it to a grayscale image, then a black and white image that is composed of the differences between the first frame and the current frame. These differences are highlighted in white. The program then proceeds to take the coordinates of these differences and box them at the correct location over the original color feed. 
