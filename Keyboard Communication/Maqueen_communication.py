import serial
import keyboard  
import time

SERIAL_PORT = 'COM9' 
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()

print("Use arrow keys to control the Maqueen. Press 'q' to quit.")

def send_command(cmd):
    ser.write(b"cmd\n")

while True:
    if keyboard.is_pressed('up'):
        print("Forward")
        ser.write(b"1\n")
        time.sleep(0.3)  
    elif keyboard.is_pressed('down'):
        print("Backward")
        ser.write(b"2\n")
        time.sleep(0.3)
    elif keyboard.is_pressed('left'):
        print("Left")
        ser.write(b"3\n")
        time.sleep(0.3)
    elif keyboard.is_pressed('right'):
        print("Right")
        ser.write(b"4\n")
        time.sleep(0.3)
        
    elif keyboard.is_pressed('q'):
        print("Exiting")
        break

ser.close()
