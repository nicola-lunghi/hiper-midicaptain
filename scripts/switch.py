# NOTE: for this example you need the adafruit_debouncer.mpy library
# from the adafruit circuitpython 7.x bundle.
# inspired by the debouncer demo in debouncer_multi.py (examples folder)

import board
import digitalio
import time
import adafruit_debouncer

switches_config = (
    ('encoderSW',  board.GP0),
    ('encoderA',   board.GP2),
    ('encoderB',   board.GP3),
    ('switch1',    board.GP1),
    ('switch2',    board.GP25),
    ('switch3',    board.GP24),
    ('switch4',    board.GP23),
    ('switchUp',   board.GP20),
    ('switchA',    board.GP9),
    ('switchB',    board.GP10),
    ('switchC',    board.GP11),
    ('switchD',    board.GP18),
    ('switchDown', board.GP19),
)

switches = dict()
for name, gpio in switches_config:
    pin = digitalio.DigitalInOut(gpio)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    switch = adafruit_debouncer.Button(pin=pin, short_duration_ms=100, long_duration_ms=1000, value_when_pressed=False)
    switches[name] = switch

print("Debouncer version=", adafruit_debouncer.__version__)

while True:
    for name, switch in switches.items():
        switch.update()
        if switch.fell:
            print(name, "Just pressed! Fell")
        if switch.rose:
            print(name, "Just released! Rose")
        if switch.long_press:
            print(name, "Long Press")
        if switch.short_count != 0:
            print(name, "Short Press Count =", switch.short_count)
        if switch.long_press and switch.short_count == 1:
            print(name, "Long double press!")
        #if switch.value is False:
        #    print(name, "pressed=", switch.value)
