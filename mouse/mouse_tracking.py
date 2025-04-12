import pyautogui as pag
import time
import serial
dev_ser = serial.Serial('COM3', 9600)  # Adjust the COM port and baud rate as needed

def read_inputs():
    try:
        line = dev_ser.readline().decode('utf-8').strip()
        if line:
            data = line.split(',')
            dx = int(data[0])
            dy = int(data[1])
            left = int(data[2])
            right = int(data[3])
            scroll_amount = int(data[4])
            return dx, dy, left, right, scroll_amount
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return 0, 0, 0, 0, 0
def move(dx, dy):
    pag.moveRel(dx, dy)
def left_click():
    pag.click()
def right_click():
    pag.rightClick()
#Optional scroll function
#def scroll(dy):
#    pag.scroll(dy)
#    Theoretically, when both left and right buttons are selected, the vertical wrist motion will be used to scroll
def scroll(scrl_amount):
    pag.scroll(scrl_amount)
def main():
    while True:
        dx, dy, left, right, scroll_amount = read_inputs()
        if dx !=0 or dy != 0:
            move(dx, dy)
        if left:
            left_click()
        if right:
            right_click()
        #Possible integration of other scroll function
        #if left and right:
        #    scroll(dy)
        if scroll_amount != 0:
            scroll(scroll_amount)
        time.sleep(0.01)
if __name__ == "__main__":
    main()
