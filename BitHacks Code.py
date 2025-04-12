import pyautogui as pag
import serial
import time
# Configure the serial port
ser = serial.Serial('Our Serial Port', 9600, timeout=1)
time.sleep(2)  #Buffer time for connection

# Alter sensor sensitivity
sensitivity = 0.1
try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                # Process the sensor data
                data = {k: int(v) for k, v in (item.split(':') for item in line.split())}
                x = data.get('X', 0)
                y = data.get('Y', 0)

                # Calculate mouse movement
                move_x = int(x * sensitivity)
                move_y = int(y * sensitivity)

                # Move the mouse
                pag.moveRel(move_x, move_y)
            except (ValueError, KeyError):
                print(f"Invalid data format: {line}")
except KeyboardInterrupt:
    print("Error Occured with Sensor Connection")
finally:
    ser.close()