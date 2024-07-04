import board
import digitalio
import time

# Pins to test for loopback (excluding known switch pins and UART1 TX)
pins_to_test = [
    # board.GP0, # SW1
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4, # uart1 tx?
    board.GP5, # uart1 rx?
    board.GP6,
    # board.GP7, # NEOPIXEL
    board.GP8,
    # board.GP12, board.GP13, # debug port?
    board.GP14,
    # board.GP15, # bootsel?
    board.GP16,
    board.GP17,
    # board.GP18, board.GP19, board.GP20, # SW
    board.GP21,
    board.GP22,
    # board.GP23, board.GP24, board.GP25, # SW
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
]

def gpio_loopback_test(tx_pin, pins_to_test):
    # Set up TX pin as output
    tx = digitalio.DigitalInOut(tx_pin)
    tx.direction = digitalio.Direction.OUTPUT

    # Set up test pins as inputs
    inputs = []
    for pin in pins_to_test:
        inp = digitalio.DigitalInOut(pin)
        inp.direction = digitalio.Direction.INPUT
        inputs.append(inp)

    # Test high value
    tx.value = True
    time.sleep(0.1)  # Small delay to ensure value is set
    print(f"Set {tx_pin} HIGH")
    for i, pin in enumerate(pins_to_test):
        print(f"Pin {pin} value: {inputs[i].value}")

    # Test low value
    tx.value = False
    time.sleep(0.1)  # Small delay to ensure value is set
    print(f"Set {tx_pin} LOW")
    for i, pin in enumerate(pins_to_test):
        print(f"Pin {pin} value: {inputs[i].value}")

# Perform loopback test on GP4
print("Performing GPIO loopback test on GP4")
gpio_loopback_test(board.GP4, pins_to_test)
