import cv2
import os
import shutil
import serial
import numpy as np
from time import sleep

#Declaring the initial values, serial port and baudrate
#ser = serial.Serial('COM6', 9600, timeout=0)
capture = cv2.VideoCapture(0)
framenumber = 0
index = 0
index0 = 0
index1 = 0

#Adjusting the video resolution
capture.set(3, 640) #Width
capture.set(4, 480) #Height

#Tries to make a directory named 'data' to store the frames
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

#Video loop
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        #Shows the video stream
        cv2.imshow('VLC', frame)

        #Store the frames as .jpg files
        img_name = './data/frame' + str(framenumber) + '.jpg'
        cv2.imwrite(img_name, frame)
        sleep(1)

        #Read the frame and store it into variable "bytes"
        data = cv2.imread('./data/frame' + str(framenumber) + '.jpg')
        np.data = np.array(data)
        print(len(np.data))    #Length of the rows
        print(len(np.data[0]))     #Length of the columns

        #ser.write(np.data)

        #Store the values into txt files
        frame_values = open("frame_value" + str(framenumber) + ".txt", "w")
        #np.savetxt('frame_value' + str(framenumber) + '.txt', np.data, delimiter=',', fmt='%d')
        frame_values.close()

        framenumber += 1

        #To stop and close the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

#Deletes the file "data" after the video finished
#shutil.rmtree('data')
