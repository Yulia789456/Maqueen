# Maqueen robot
## Project description

For this project, you will need:
* 1x DFRobot Maqueen
* 2x Microbit boards (Maqueen microbit, transmit/receiver microbit)
* 1x USB cable to connect transmit microbit to your PC

This project allows the Maqueen robot (which uses a microbit) to be controlled wirelessly using your computer keyboard, with communication handled through two microbit boards using radio signals and serial communication. Transmit microbit (connected to your PC via USB) receives keyboard inputs from your PC using serial communication and then sends radio signals to maqueen microbit (connected to your robot). Maqueen microbit listens to incoming radio commands and controls the robot's motor using the maqueen.py module (Up Arrow for moving forward, Down Arrow for moving backwards, Right Arrow for moving right and Left Arrow for moving left). The maqueen.py module provides all the functions to control the robot. 

You can also control the robot with a transmit microbit's button, button A for moving forward, button B for moving backwards and A + B for turning. 

## Functions used
## Keyboard Communication
### def send_comman(cmd) 
This function was defined to send commands directly using ser.write() inside the while loop. The send_command function could be used to simplify the code, but the script works without it. So it could be safely removed. 

## Maqueen microbit board
### def drive_command(cmd)
This function gets a number (from 1 to 4) and runs the motor in the correct direction: 1 - forward, 2 - backward, 3 - left, and 4 - right. It uses motor control methods and the display to show the direction (F, B, L, R), waits and then stops the motor. 

The main while True loop waits for radio messages from the transmitter board, then passes the number to drive_command().

## Transmit/receiver microbit board
This board does not use any functions. Only a while loop listening to a serial input from the PC.

It also allows the control of the Maqueen robot using the A and B buttons on the microbit directly as a backup. 

## The requirements (pip freeze)
See requirements.txt 

These dependencies are open source and licensed under permissive licenses such as MIT, BSD, and Apache 2.0. They allow you to use them in personal and commercial projects, but you should retain their license notices if you distribute your project.

For the receiver microbit, you will need the maqueen.py module.

## Licence
The licensing information on DFRobot’s GitHub shows that it uses the MIT open-source license.

For this project, I also have adopted the MIT Open-Source license.

For more information, see the LICENCE file.
