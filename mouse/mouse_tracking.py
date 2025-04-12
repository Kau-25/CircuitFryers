import pyautogui as pag
import time
import serial
dev_ser = serial.Serial('COM3', 9600) 

def read_inputs():
    try:
        line = dev_ser.readline().decode('utf-8').strip()
        if line:
            data = line.split(':')
            accel_x = int(data[0])
            accel_y = int(data[1])
            accel_z = int(data[2])
            # gyro_x = int(data[3])
            # gyro_y = int(data[4])
            # gyro_z = int(data[5])
            return accel_x, accel_y #, gyro_x, gyro_y
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return 0, 0, 0, 0
def move(dx, dy):
    pag.moveRel(dx, dy)
# def find_vector(accel, gyro):
#     v = None
#     return v
# def left_click():
#     pag.click()
# def right_click():
#     pag.rightClick()
# def scroll(dy):
#     pag.scroll(dy)
def main():
    while True:
        accel_x, accel_y = read_inputs()
        # accel_x, accel_y, gyro_x, gyro_y = read_inputs()
        # x_vector = find_vector(accel_x, gyro_x)
        # y_vector = find_vector(accel_y, gyro_y)
        if accel_x !=0 or accel_y != 0:
            move(accel_x, accel_y)
        # if left:
        #     left_click()
        # if right:
        #     right_click()
        # if left and right:
        #     scroll(dy)
        time.sleep(0.01)
if __name__ == "__main__":
    main()
