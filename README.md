# Visible-Light-Communication

An embedded systems project for sending image via light with using two Arduino Uno's 

Purpose of this project is to use a simple software to send data with visible light.

System gets an image data from one arduino UNO ( transmitter side ) and sends this data via visible light ( using LED and LDR )
to another arduino UNO ( receiver side ) to convert this data back to an image.

-Software of Microprocessors and Computer Program (Not the final version)
Software part is crucial in VLC (Visible Light Communication ) in order to transmit/receive data precisely and accurately in VLC systems.
1.Transmitter Side
  After the image signal gets to Arduino, ADC(Analog to Digital Converter) converts the incoming signal amplitude into 10bit value( default in Arduino UNO ), this value   is converted again into an array of 8bits since every frame and every pixel of these frames consists 8bits of information.
  In order to get the amplitude value after ADC is finished, system uses a trick called interrupt service routine(ISR) otherwise ADC will get all the data until the       Arduino is out  of memory.
2.Receiver Side
  Receiver part starts with the incoming digital signal from LDR pin, if the signal is bigger than the threshold of the inner resistor of Arduino’s digital pin ( i.e if   the incoming light is more than the real life exposure that is effecting the LDR ) the system considers this change as a bit of ‘1’ 
  otherwise bit is  considered to be ‘0’.
  After receiving 8 bits, these bits are stored inside an array.
3.Computer Program
  Final part of the system consists of only a python program that runs on the computer that the receiver is connected with USB cable, this could also be any other system   with a display that can run the same program.
  First part of the program is to get the raw data that is received after the transmisson from USB cable, for that a library called ‘Serial.py’ is used. Serial             command receives information in hexadecimal values and these hex values are converted into decimal values to get the pixel value of the transmitted image for that       specific pixel, these values are stored in an [320][240] array since image resolution that has been used for this project is ‘320 x 240’.
  After all the pixel values are received from the USB port and corresponded with the correct pixel, program uses the ‘Opencv’ library to convert these values into a       black and white image.

