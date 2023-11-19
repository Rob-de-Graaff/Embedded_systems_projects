from neopixel import Neopixel
from time import sleep

NUM_LEDS = 16
LED_PIN = 28
pixels = Neopixel(NUM_LEDS, 0, LED_PIN, "GRB")
pixels.brightness(255)

orange1 = (255, 165, 0)
orange2 = (255, 153, 0)

for led in range(NUM_LEDS):
    if led % 2 is 0:
        pixels.set_pixel(led, orange1)
    else:
        pixels.set_pixel(led, orange2)
pixels.show()

###########################################################

from neopixel import Neopixel
import time

NUM_LEDS = 16
LED_PIN = 28
pixels = Neopixel(NUM_LEDS, 0, LED_PIN, "RGB")
pixels.brightness(255)

# RED = 255 RED, 0 GREEN, 0 BLUE
# ORANGE = 255 RED, 153(165) GREEN, 0 BLUE

color = [0, 255, 0]
# pixels.fill(color)
# pixels.show()
increment = 0.1 # OR use time.sleep()
minValue = 0
maxValue = 165
while True:
    color[0] += increment

    print(increment)
    if color[0] >= maxValue:
        color[0] = maxValue
        increment = -1 * increment

    if color[0] <= minValue:
        color[0] = minValue
        increment = -1 * increment

    pixels.fill(color)
    print(color)
    pixels.show()
    # time.sleep(0.1)

################################################################

import time 
from neopixel import Neopixel

steps = 100
numpix = 16 # number of LEDs in the strip 
pixels = Neopixel(numpix, 0, 28, "RGB") # create a NeoPixel object on pin 28

def fade_between(hue_start, hue_end, gradient):
  for i in range(gradient): 
    hue = hue_start + (hue_end - hue_start) * i / gradient # interpolate the hue 
    color = (hue, 255, 0) # convert hue to RGB color 
    print(color)
    pixels.fill(color) 
    pixels.show()
    time.sleep(0.1)

while True: 
  fade_between(0, 165, steps) # fade from red to orange 
  fade_between(165, 0, steps) # fade from orange to red