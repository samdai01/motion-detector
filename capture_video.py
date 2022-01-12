# ***********************************************************************************************************
# Video capture and motion detection script.
# Written by Sam Dai 
# ***********************************************************************************************************


# Library imports:
#   cv2 - OpenCV library which contains the required programs for detecting and finding objects.
#   time - To manage the time since the last minute for the graph output.
#   pandas - To build the csv file that contains the start time and end time data.
import cv2
import time
import pandas


startTime = time.time()     # time of initial execution.
firstFrame = None   # background to compare moving objects in frame to
motionStatus = [None, None]     
motionTimes = []    # Stores enter and exit times of objects. 
dataFrame = pandas.DataFrame(columns=["Start Times", "End Times"])  # Pandas dataframe that stores motionTimes data for plotting.

videoFeed = cv2.VideoCapture(0) # Set VideoCapture parameter to 0 if onboard camera is uesd.

while True:
    check, frame = videoFeed.read()
    motionStatusValue = False    
    grayFeed = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   # Converts input feed to grayscale.
    grayFeed = cv2.GaussianBlur(grayFeed, (21, 21), 0) # Blurs the image to improve accuracy.
    
    # Sets the background frame.
    if firstFrame is None: 
        firstFrame = grayFeed
        continue
    
    # Highlights the difference of the current frame compared with the original background frame.
    compareDiff = cv2.absdiff(firstFrame, grayFeed) 
                                           
    threshold = cv2.threshold(compareDiff, 30, 255, cv2.THRESH_BINARY)[1]
    
    threshold = cv2.dilate(threshold, None, iterations = 3)
    
    # OpenCV method that finds any moving object not originally part of background.
    (contour,_) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cont in contour:
        
        # Skips the highlighting of very small insignificant objects such as shadows.
        if cv2.contourArea(cont) < 1000:
            continue
        
        motionStatusValue = True
        
        # Creates and overlays the rectangle over found objects.
        (x_coord, y_coord, width, height) = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x_coord, y_coord), (x_coord + width, y_coord + height), (0, 255, 0), 3)
        cv2.rectangle(grayFeed, (x_coord, y_coord), (x_coord + width, y_coord + height), (0, 255, 0), 3)
        cv2.rectangle(compareDiff, (x_coord, y_coord), (x_coord + width, y_coord + height), (0, 255, 0), 3)
        cv2.rectangle(threshold, (x_coord, y_coord), (x_coord + width, y_coord + height), (0, 255, 0), 3)
    
    
    motionStatus.append(motionStatusValue)   
    
    motionStatus = motionStatus[-2:] 
    
    # Checks if input feed has a change in the feed compared to background.
    if motionStatus[-1] is True and motionStatus[-2] is False:
        motionTimes.append((time.time() - startTime) * 1000)
    
    if motionStatus[-1] is False and motionStatus[-2] is True:
        motionTimes.append((time.time() - startTime) * 1000)
          
    
    # Shows the video feed in windows. Uncomment below to include filters over feed.
    # cv2.imshow("Video Feed", grayFeed)
    # cv2.imshow("Delta", compareDiff)
    # cv2.imshow("Threshold", threshold) 
    cv2.imshow("Frame", frame)
    
    # Stores any pressed key and quits program if q key is pressed.
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        if motionStatus[-1] is True:
            
            motionTimes.append((time.time() - startTime) * 1000)
        break
    else:
        continue
    
# Takes object entry and exit times and stores them in a Pandas dataframe. Optional to store in csv.
for starts in range(0, len(motionTimes), 2):
    dataFrame = dataFrame.append({"Start Times" : motionTimes[starts], "End Times" : motionTimes[starts + 1]}, ignore_index = True)
    
dataFrame.to_csv("MotionTimes.csv")    

videoFeed.release()
cv2.destroyAllWindows()

