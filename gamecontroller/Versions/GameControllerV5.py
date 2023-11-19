import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#from adafruit_debouncer import Debouncer

btn1_pin = board.GP15
btn2_pin = board.GP16
btn3_pin = board.GP14
btn4_pin = board.GP18
btn5_pin = board.GP13
btn6_pin = board.GP17

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn2 = digitalio.DigitalInOut(btn2_pin)
btn3 = digitalio.DigitalInOut(btn3_pin)
btn4 = digitalio.DigitalInOut(btn4_pin)
btn5 = digitalio.DigitalInOut(btn5_pin)
btn6 = digitalio.DigitalInOut(btn6_pin)

btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT
btn5.direction = digitalio.Direction.INPUT
btn6.direction = digitalio.Direction.INPUT

# depending to the pin config Pull.DOWN OR Pull.UP
btn1.pull = digitalio.Pull.DOWN
btn2.pull = digitalio.Pull.DOWN
btn3.pull = digitalio.Pull.DOWN
btn4.pull = digitalio.Pull.DOWN
btn5.pull = digitalio.Pull.DOWN
btn6.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("Button O pressed")
        #keyboard.send(Keycode.O,)

        keyboard.press(Keycode.O,)
        #time.sleep(0.1)
        keyboard.release(Keycode.O,)

    if btn2.value:
        print("Button P pressed")
        #keyboard.send(Keycode.P,)

        keyboard.press(Keycode.P,)
        #time.sleep(0.1)
        keyboard.release(Keycode.P,)

    if btn3.value:
        print("Button Down pressed")
        #keyboard.send(Keycode.DOWN_ARROW,)

        keyboard.press(Keycode.DOWN_ARROW,)
        #time.sleep(0.1)
        keyboard.release(Keycode.DOWN_ARROW,)

    if btn4.value:
        print("Button Right pressed")
        #keyboard.send(Keycode.RIGHT_ARROW,)

        keyboard.press(Keycode.RIGHT_ARROW,)
        #time.sleep(0.1)
        keyboard.release(Keycode.RIGHT_ARROW,)
        
    if btn5.value:
        print("Button Up pressed")
        #keyboard.send(Keycode.UP_ARROW,)

        keyboard.press(Keycode.UP_ARROW,)
        #time.sleep(0.1)
        keyboard.release(Keycode.UP_ARROW,)
    
    if btn6.value:
        print("Button Left pressed")
        #keyboard.send(Keycode.LEFT_ARROW,)

        keyboard.press(Keycode.LEFT_ARROW,)
        #time.sleep(0.1)
        keyboard.release(Keycode.LEFT_ARROW,)
        
    #time.sleep(0.1)