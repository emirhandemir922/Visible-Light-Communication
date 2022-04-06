import cv2
import serial
import numpy as np
import codecs
import time

arduinoserial = serial.Serial('COM6 ', baudrate=1000000)    #serial command to get hexadecimal values from USB port
                                                            #important note : 'COM3' is representing the port that the system is connected
                                                            #and baudrate is the one that is defined in the 'Receiver.ino', these two inputs must
                                                            #be right in order to get the correct data from USB port.

frame_values = np.empty([240, 320], dtype=int)              #defining an empty numpy array to store the received pixel values

def read_pixel_value():                                     #function to get the pixel value
    for counteri in range(240):                             #for loop from 0 to 240 for the y axis of the image
        for counterj in range(320):                        #for loop from 0 to 320 for the x axis of the image
            frame_values[counteri, counterj] = int(codecs.encode(arduinoserial.readline(1),"hex"), 16)      #
            print(frame_values[counteri, counterj])


elapsedtime = time.time()                                   #time function is used to measure the elapsed time for 1 image not necessary all the time
read_pixel_value()                                          #calling the function to get the pixel values

data_file = open("framevalues.txt", "w")                    #writing the all the pixel values that received to make a full image
for row in frame_values:                                    #to a txt file for debugging purposes
    np.savetxt("framevalues.txt", frame_values, fmt='%d')

cv2.imshow("received_image", frame_values)                 #creating a full black and white image with the values stored in frame_values array
elapsedtime = time.time() - elapsedtime                     #calculating elapsed time
print(elapsedtime)                                          #printing the time to the console