import cv2
import serial
import numpy as np
import codecs
import time

arr_bits = [0, 0, 0, 0, 0, 0, 0, 0]
arduinoserial = serial.Serial('COM6', baudrate=1000000)
frame_values = np.empty([240, 320], dtype=int)
threshold = 20

def read_pixel_value():
    for counteri in range(240):
        for counterj in range(320):
            for data_index in range(8):
                data_hex = arduinoserial.readline(1)
                data_hexc = codecs.encode(data_hex, "hex")  # Reads hexadecimal value from arduino
                data_int = int(data_hexc, 16)
                if  data_int > threshold:  # Compares the hexadecimal value with threshold = 50
                    arr_bits[data_index] = 1
                else:
                    arr_bits[data_index] = 0
            pixel_value = 0
            for bit_index in arr_bits:   # Bit shifting for converting the byte to integer value
                pixel_value = (pixel_value << 1) | bit_index
            frame_values[counteri, counterj] = pixel_value

elapsedtime = time.time()
read_pixel_value()
elapsedtime = time.time() - elapsedtime
print(elapsedtime)

