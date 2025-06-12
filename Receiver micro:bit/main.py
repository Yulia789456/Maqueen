from microbit import *
import radio

radio.on()
radio.config(group=1)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("turn")
        display.show("T")
        sleep(500)
        display.clear()
    elif button_a.was_pressed():
        radio.send("forward")
        display.show("F")
        sleep(500)
        display.clear()
    elif button_b.was_pressed():
        radio.send("backward")
        display.show("B")
        sleep(500)
        display.clear()
    
        
    # serial messages
    if uart.any():
        serial_data = uart.readline()
        if serial_data:
            try:
                cmd = serial_data.decode().strip()
                if cmd == "1":
                    radio.send("forward")
                    display.show("F")
                elif cmd == "2":
                    radio.send("backwards")
                    display.show("B")
                elif cmd == "3":
                    radio.send("left")
                    display.show("L")
                elif cmd == "4":
                    radio.send("right")
                    display.show("R")
            except:
                pass

