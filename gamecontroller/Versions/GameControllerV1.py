import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

btn1_pin = board.GP0
btn2_pin = board.GP5
btn3_pin = board.GP10
btn4_pin = board.GP15

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn2 = digitalio.DigitalInOut(btn2_pin)
btn3 = digitalio.DigitalInOut(btn3_pin)
btn4 = digitalio.DigitalInOut(btn4_pin)

btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT

btn1.pull = digitalio.Pull.DOWN
btn2.pull = digitalio.Pull.DOWN
btn3.pull = digitalio.Pull.DOWN
btn4.pull = digitalio.Pull.DOWN


while True:
    if btn1.value:
        print("Button 1 pressed")
        #keyboard.send(Keycode.A,)

        keyboard.press(Keycode.A,)
        #time.sleep(0.1)
        keyboard.release(Keycode.A,)

    if btn2.value:
        print("Button 2 pressed")
        #keyboard.send(Keycode.B,)

        keyboard.press(Keycode.B,)
        #time.sleep(0.1)
        keyboard.release(Keycode.B,)

    if btn3.value:
        print("Button 3 pressed")
        #keyboard.send(Keycode.C,)

        keyboard.press(Keycode.C,)
        #time.sleep(0.1)
        keyboard.release(Keycode.C,)

    if btn4.value:
        print("Button 4 pressed")
        #keyboard.send(Keycode.D,)

        keyboard.press(Keycode.D,)
        #time.sleep(0.1)
        keyboard.release(Keycode.D,)
    
    #time.sleep(0.1)