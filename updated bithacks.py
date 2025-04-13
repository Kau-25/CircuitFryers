import pyautogui as pag
import time
import serial
import keyboard


mouse_click_status = 0 #Tracks if mouse is pressed or not
scroll_desenser = 20 #manages sensitivity of scroll
timer = 0.001 #Delay between loops
mouse_lock_buffer = 0
mouse_lock_status = False #If the mouse is clicked three times in a row, within this certain duration, the mouse will be locked in place
dev_ser = serial.Serial('COM9', 115200)
def read_inputs():
    try:
        data = dev_ser.read_all().decode('utf-8')
        lines = data.strip().split('\n')
        if not lines or lines[-1].strip() == "":
            return 0, 0, 0, 0, 0
        line = lines[-1].strip()
        if line:
            data = line.split(':')
            accel_x = int(data[0])
            accel_y = int(data[1])
            accel_z = int(data[2])
            joystick_x = int(data[3])-2900
            joystick_y = int(data[4])-2840
            joystick_press = int(data[5])
            return accel_x, accel_y, joystick_x, joystick_y, joystick_press
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return 0, 0, 0, 0, 0
def move(x_vector, y_vector):
    pag.moveRel(x_vector, y_vector) #Moves the mouse based on x-y vectors
def mouse_down():
    global mouse_click_status
    pag.mouseDown() #Presses the mouse down
    mouse_click_status = 1
def mouse_up(): #Lifts the mouse
    global mouse_click_status
    pag.mouseUp()
    mouse_click_status = 0
def right_click(): #Right clicks the mouse
    pag.rightClick()
def scroll(scroll_value): #Scrolles the mouse up and down
    pag.scroll(scroll_value)
def main():
    global mouse_click_status, mouse_lock_buffer, mouse_lock_status
    #Main loop
    while True:
        #Gather inputs
        accel_x, accel_y, joy_x, joy_y, press = read_inputs()
        #Move mouse
        if (accel_x >20 or accel_x<-20 or accel_y >20 or accel_y<-20) and mouse_lock_status == False:
            print(f"Accel X: {accel_x}, Accel Y: {accel_y}")
            #Calibrate vectors to fit user's perspecitve of peripherals
            x_vector = accel_y * 1
            y_vector = accel_x * -1
            joy_y = joy_y * -1
            move(x_vector, y_vector)
        #Mouse press
        if joy_y<=1000 and press: #If the joystick is pressed and is not moved to the right
            mouse_down()
        if not press and mouse_click_status == 1: #If the joystick is no longer pressed
            mouse_up()
        if joy_y>=1000 and press: #If the joystick is pressed and is moved to the right
            right_click()
        if joy_x>=500 or joy_x<=-500: #If the joystick is past the vertical threshold
            scroll(int(joy_x/scroll_desenser)) #Buffers scrolling to control sensitivity
        time.sleep(timer)#Sleeps before the next iteration of the loop to control refresh rate
        #Mouse lock
        if keyboard.is_pressed('p') and mouse_lock_buffer == 0: #If the 'p' key is pressed and the buffer is empty
            mouse_lock_status = not mouse_lock_status #If the 'p' key is pressed, toggle mouse lock status
            mouse_lock_buffer = 2000
        if mouse_lock_buffer > 0:
            mouse_lock_buffer -= 20
if __name__ == "__main__":
    main()


