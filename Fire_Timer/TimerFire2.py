from machine import Pin, Timer

notificationLed = Pin(18, Pin.OUT) # Use GP13
button = Pin(28, Pin.IN, Pin.PULL_DOWN) # Use GP18

notificationLed.value(0)
timer=Timer(-1) # init timer with id=-1

timeInMiliseconds = 5000 # global variable

def set_timer(miliseconds):
    print('set timer')
    timer.init(period=miliseconds, mode=Timer.ONE_SHOT, callback=push_notification)
    
def push_notification(timer):
    print('set LED')
    timer.init(period=500, mode=Timer.PERIODIC, callback=lambda t:notificationLed.value(not notificationLed.value()))

def debounce(pin):
    # Start or replace a timer for 200ms, and trigger on_pressed.
    timer.init(mode=Timer.ONE_SHOT, period=200, callback=on_pressed)

def on_pressed(change):
    print('button pressed')
    notificationLed.value(0)    
    set_timer(timeInMiliseconds)

# Register an interrupt on falling button input.
button.irq(handler=debounce, trigger=Pin.IRQ_FALLING)

set_timer(timeInMiliseconds)