# CircuitFryers

We used the Arduino IDE to create sensor_input.ino, which takes in sensor data via the ESP32 and sends it over the Serial line via USB. 
The Arduino file utilizes the FastIMU.h library to recieve data from the gyroscope, and the Wire library.

The python file code recieves this data, and translates it into mouse movement/clicks/scrolling.
The python code utilizes the pyautogui library to control mouse output, the serial library to receive data, the time library for input buffers, and the keyboard library to take in the pause button 'p' input (to freeze mouse movement).
