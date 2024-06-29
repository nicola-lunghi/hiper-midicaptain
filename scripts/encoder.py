# From https://learn.adafruit.com/rotary-encoder/circuitpython

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import adafruit_debouncer
import board
import digitalio
import rotaryio

encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)

# switch
pin = digitalio.DigitalInOut(board.GP0)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
switch = adafruit_debouncer.Button(
    pin=pin,
    short_duration_ms=100,
    long_duration_ms=1000,
    value_when_pressed=False
)

last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position

    # switch
    switch.update()
    if switch.fell:
        print("Encoder Pressed! Fell")
    if switch.rose:
        print("Encoder Released! Rose")
