import digitalio
import usb_hid
from adafruit_hid.gamepad import Gamepad
from time import sleep
import board
            
gamepad = Gamepad()

button_status = {'up' : 0, 'down' : 0, 'left' : 0, 'right' : 0}
buttons = {0 : 'up', 1 : 'down', 2 : 'left', 3 : 'right'}

#latch = digitalio.DigitalInOut(board.GP5)
#clock = digitalio.DigitalInOut(board.GP4)
#data = digitalio.DigitalInOut(board.GP6)

#latch.direction = digitalio.Direction.OUTPUT
#clock.direction = digitalio.Direction.OUTPUT
#data.direction = digitalio.Direction.INPUT

#data.pull = digitalio.Pull.UP

#latch.value = False
#clock.value = False
previousState = False

delaytime = 0.0001

while True:
    latch.value = True
    sleep(delaytime)
    latch.value = False
    sleep(delaytime)
    button_status[buttons[0]] = data.value
    
    for x in range(0, 7, 1):
        clock.value = True
        sleep(delaytime)
        clock.value = False
        sleep(delaytime)
        button_status[buttons[x + 1]] = data.value
        
    press_buttons = []
    release_buttons = []
    
    for x in buttons:
        if button_status[buttons[x]] == True:
            gamepad.release_buttons(x + 1)
        else:
            gamepad.press_buttons(x + 1)