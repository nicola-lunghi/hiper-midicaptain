import board
import neopixel
import time

# List of GPIO pins to test for Neopixel control
gpio_pins = [
    board.GP1, board.GP2, board.GP3, board.GP6, board.GP7, board.GP8,
    board.GP14, board.GP16, board.GP17, board.GP21, board.GP22,
    board.GP26, board.GP27, board.GP28
]

def test_neopixel_pin(pixels):
    try:
        pixels.fill((255, 0, 0))  # Red
        pixels.show()
        time.sleep(0.5)

        pixels.fill((255, 255, 0))  # Red
        pixels.show()
        time.sleep(0.5)

        pixels.fill((0, 255, 255))  # Red
        pixels.show()
        time.sleep(0.5)

        pixels.fill((0, 0, 255))  # Red
        pixels.show()
        time.sleep(0.5)

        pixels.fill((0, 0, 0))  # Turn off
        pixels.show()
        time.sleep(0.5)
    except Exception as e:
        print(f"Error testing {pin}: {e}")

pin = board.GP7
num_pixels = 30
pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False)

# Test each GPIO pin for Neopixel control
while True:
    print(f"Testing {pin}")
    test_neopixel_pin(pixels)
    time.sleep(1)
