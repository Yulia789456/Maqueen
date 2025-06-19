# Maqueen
## Implementation phase

For this project you will needed:
* 1x DFRobot Maqueen
* 2x Microbit boards (Maqueen microbit, transmit/receiver microbit)
* 1x USB cable to connect transmit microbit to your PC

This project allows Maqueen robot (which uses a microbit) to be controlled wirelessly using your computer keyboard, with communication handled thought two microbit boards using radio signals and serial communication. Transmit microbit (connected to your PC via USB) received keyboard inputs from your PC using serial communication, and then sends radio signals to maqueen microbit (connected to your robot). Maqueen microbit listens to incoming radio commands and control the robots motor using maqueen.py module (Up Arrow for moving farward, Down Arrow for moving backwards, Right Arrow for moving right and Left Arrow for moving left). The maqueen.py module provides all the functions to control the robot. 

You can also control the robot with transmit microbit's button, button A for moving farward, button B for moving backwards and A + B for turning. 

# Functions used
## Keyboard Communication
### def send_comman(cmd) 
This function was defined to send commands directly using ser.write() inside the while loop. The send_command function could be used to simplify the code but the script works without it. So, it could be safely removed. 

## Maqueen microbit board
### def drive_command(cmd)
This function gets a number (from 1 to 4) and runs motor in correct direction: 1 - farward, 2 - backward, 3 - left, 4 - right. It uses motor control methods and the display to show the direction (F, B, L, R), waits and then stops the motor. 

Main while True loop waits for radio messages from transmitter board, then passes the number to drive_command().

## Transmit/receiver microbit board
This board does not used any functions. Only a while loop listening to a serial input from the PC.

It also allows control Maqueen robot using A and B buttons on the microbit directly as a backup. 

## The requirements (pip freeze)
See requirements.txt 

These dependencies are open source and licensed under permissive licenses such as MIT, BSD, and Apache 2.0. They allow to use them in personal and commercial projects, but you should retain their license notices if you distribute your project.

For receiver microbit you will need maqueen.py module.

# Licence
According to the GitHub of DFRobot, it is licensed under an MIT Open-Source license.

For this project I also have adopted MIT Open-Source license

For more information see LICENCE file
