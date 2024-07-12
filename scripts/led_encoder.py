import board
import neopixel
import time

import digitalio
import rotaryio

neo_pin = board.GP7
num_pixels = 30

ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(neo_pin, num_pixels, auto_write=False)

encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def set_rainbow(position):
    rgb = wheel(position & 255)
    print(f"Position={position}; Color=0x{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    for i in range(num_pixels):
        pixels[i] = rgb
    pixels.show()

last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        set_rainbow(position)
    last_position = position
