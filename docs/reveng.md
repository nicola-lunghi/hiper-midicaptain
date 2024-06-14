# Introduction

This is a tentative alternative firmware for the Paint Audio Midi Captain.
This is based on reverse engineering, and is make available to the public hoping it will be useful.

# Board Description

The board is based on a Raspberry Pi Core Microcontroller, with the following peripherals:

- 10 footswitches
- Midi In/Out
- 2 expression pedal Input
- 30  RGB led, separately addressables
- Battery

# GPIO Assignment

| GPIO    | PERIPERAL                 | PIN FUNCTION         |
|---------|---------------------------|----------------------|
| GP0     | switch                    | sw1                  |
| GP1     |                           |                      |
| GP2     |                           |                      |
| GP3     |                           |                      |
| GP4     | (uart_midi_tx?)           |                      |
| GP5     | (uart_midi_rx?)           |                      |
| GP6     |                           |                      |
| GP7     |                           |                      |
| GP8     |                           |                      |
| GP9     | switch                    | swA                  |
| GP10    | switch                    | swB                  |
| GP11    | switch                    | swC                  |
| GP12    | (debug_port??)            |                      |
| GP13    | (debug_port??)            |                      |
| GP14    |                           |                      |
| GP15    | (bootsel_pin???)          |                      |
| GP16    |                           |                      |
| GP17    |                           |                      |
| GP18    | switch                    | swD                  |
| GP19    | switch                    | swDN                 |
| GP20    | switch                    | swUP                 |
| GP21    |                           |                      |
| GP22    |                           |                      |
| GP23    | switch                    | sw4                  |
| GP24    | switch                    | sw3                  |
| GP25    | switch                    | sw2                  |
| GP26    |                           |                      |
| GP27    |                           |                      |
| GP28    |                           |                      |
| GP29    |                           |                      |

# Reverse engineering code

## Midi UART

### Uart Pins

UART pins can be assigned to any GPIO. default pinout for Raspberry pi pico board:
- UART0:
  - board.GP0 (TX)
  - board.GP1 (RX)
- UART1:
  - board.GP4 (TX)
  - board.GP5 (RX)

### Gpio Loopback Test

1. set a midi cable between midi in and out
2. run the following

  ```python
  import board
  import digitalio
  import time

  # Pins to test for loopback (excluding known switch pins and UART1 TX)
  pins_to_test = [
      # board.GP0, # SW1
      board.GP1, board.GP2, board.GP3,
      # board.GP5, # uart1 rx?
      board.GP6, board.GP7, board.GP8,
      # board.GP12, board.GP13, # debug port?
      board.GP14,
      # board.GP15, # bootsel?
      board.GP16, board.GP17,
      # board.GP18, board.GP19, board.GP20, # SW
      board.GP21, board.GP22,
      # board.GP23, board.GP24, board.GP25, # SW
      board.GP26, board.GP27, board.GP28, board.GP29,
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
  ```

## Neopixel Led

30 RGB led on the board.

### Test Code

```python
import board
import neopixel
import time

# List of GPIO pins to test for Neopixel control
gpio_pins = [
    board.GP1, board.GP2, board.GP3, board.GP6, board.GP7, board.GP8,
    board.GP14, board.GP16, board.GP17, board.GP21, board.GP22,
    board.GP26, board.GP27, board.GP28
]

# Number of Neopixels
num_pixels = 30

def test_neopixel_pin(pin):
    try:
        pixels = neopixel.NeoPixel(pin, num_pixels, auto_write=False)
        pixels.fill((255, 0, 255))  # Red
        pixels.show()
        time.sleep(0.5)
        pixels.fill((0, 0, 0))  # Turn off
        pixels.show()
        print(f"Neopixels test pin {pin}")
    except Exception as e:
        print(f"Error testing {pin}: {e}")

# Test each GPIO pin for Neopixel control
for pin in gpio_pins:
    print(f"Testing {pin}")
    test_neopixel_pin(pin)
    time.sleep(1)
```

## Display

## Wireless Module



# Test code


### Gpio Loopback Test

1. set a midi cable between midi in and out
2. run the following

  ```python
  import board
  import digitalio
  import time

  #   1          2           3           4           UP/DWN
  switch_pins = [
      board.GP0, board.GP25, board.GP24, board.GP23, board.GP20,
      board.GP9, board.GP10, board.GP11, board.GP18, board.GP19,
  ]

  # Pins to test for loopback (excluding known switch pins and UART1 TX)
  pins_to_test = [
      board.GP1, board.GP2, board.GP3,
      # board.GP5, # uart1 rx?
      board.GP6, board.GP7, board.GP8,
      # board.GP12, board.GP13, # debug port?
      board.GP14,
      # board.GP15, # bootsel?
      board.GP16, board.GP17,
      board.GP21, board.GP22,
      board.GP26, board.GP27, board.GP28, board.GP29,
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
  ```
