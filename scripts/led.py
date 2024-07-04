import board
import neopixel
import time

def set_color(pixels, color):
    pixels.fill(color)
    pixels.show()

def test_neopixel_pin(pixels):
    try:
        set_color(pixels, (255, 0, 0))
        time.sleep(0.5)
        set_color(pixels, (255, 255, 0))
        time.sleep(0.5)
        set_color(pixels, (0, 255, 255))
        time.sleep(0.5)
        set_color(pixels, (0, 0, 255))
        time.sleep(0.5)
        set_color(pixels, (0, 0, 0))  # Turn off
        time.sleep(0.5)
    except Exception as e:
        print(f"Error testing {pin}: {e}")

neo_pin = board.GP7
num_pixels = 30
pixels = neopixel.NeoPixel(neo_pin, num_pixels, auto_write=False)

# Test each GPIO pin for Neopixel control
while True:
    print(f"Testing {neo_pin}")
    test_neopixel_pin(pixels)
    time.sleep(1)
