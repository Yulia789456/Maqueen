from microbit import *
from maqueen import Maqueen
import radio
import time

robot = Maqueen()

radio.on()
radio.config(group=1)

def drive_command(cmd):
    if cmd == 1:
        display.show("F")
        robot.motor_left(300, 0)
        robot.motor_right(300, 0)
        sleep(1000)
        robot.motor_left(0, 0)
        robot.motor_right(0, 0)
        display.clear()
    elif cmd == 2:
        display.show("B")
        robot.motor_left(300, 1)
        robot.motor_right(300, 1)
        sleep(1000)
        robot.motor_left(0, 0)
        robot.motor_right(0, 0)
        display.clear()
    elif cmd == 3:
        display.show("L")
        robot.motor_left(50, 0)
        robot.motor_right(100, 1)
        sleep(400)
        robot.motor_left(0, 0)
        robot.motor_right(0, 0)
        display.clear()
    elif cmd == 4:
        display.show("R")
        robot.motor_left(100, 1)
        robot.motor_right(50, 0)
        sleep(400)
        robot.motor_left(0, 0)
        robot.motor_right(0, 0)
        display.clear()

while True:
    # radio messages
    msg = radio.receive()
    if msg == "forward":
        drive_command(1)
    elif msg == "backward":
        drive_command(2)
    elif msg == "left":
        drive_command(3)
    elif msg == "right":
        drive_command(4)



