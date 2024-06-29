# Introduction

This is a tentative to reverse engineer/develop alternative firmwares for the [Paintaudio Midi Captain](https://paintaudio.com/products/paint-audio-midi-captain-blue).

This is based on reverse engineering, and is make available to the public hoping it will be useful, but
I offer

**no warranty whatsoever on anything (if you break it YOU ARE ON YOUR OWN!!!!)**.

This infomation is similar to other Paintaudio products:
- [Midi Captain STD Version Black](https://paintaudio.com/products/midi-captain-std-vesion-black) (Same with no wireless module)
- [Midi Captain Mini 6](https://paintaudio.com/products/midi-captain-mini-6-controller-with-hid-multi-state-cycling)
- [Midi Captain Nano 4](https://paintaudio.com/products/midi-captain-nano-4-controller-with-hid-multi-state-cycling)
- [Midi Captain Duo](https://paintaudio.com/products/midi-captain-duo-controller-with-hid-multi-state-cycling-1)
- [Midi Captain One](https://paintaudio.com/products/midi-captain-one-controller-with-hid-multi-state-cycling-1)

that seems to be based on the same microcontroller (RP2040) and CircuitPython.
But not having them I cannot verify the information.

# General Description

The board is based on a Raspberry Pi Core Microcontroller ([RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)) and is programmed using [CircuitPython](https://circuitpython.org).

The CircuitPython Version on the board as per firmware 4.0 is 7.3.1 (see boot_out.txt)

Links:
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [CircuitPython](https://circuitpython.org)
- [Paintaudio Recover uf2 file](https://cdn.shopify.com/s/files/1/0656/8312/8548/files/midicpPico.uf2)
- [CircuitPython 7.x Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20231003/adafruit-circuitpython-bundle-7.x-mpy-20231003.zip)
- [Paintaudio Midi Captain 3in1 Firmware 4.0](https://cdn.shopify.com/s/files/1/0656/8312/8548/files/FW-MIDICP-10-switch-3in1-V4.0.zip?v=1712483089)

## Going into update mode

As described in the main product page [here](https://paintaudio.com/products/paint-audio-midi-captain-blue), to modify the CircuitPython code you have to enter the Update Mode

On the MIDI Captain this is done pressing switch0 (top left switch) when powering up while being connected via usb to a computer.
This will show you the MIDICAPTAIN drive where you can load new firmware and modify the code.

## Going into circuitpython bootloader mode

On the board there's a 2 pin header that if you short it and reboot you'll go into circuitpython recovery mode.

**Don't mess with it if you don't know what you are doing.**

- [Paintaudio Recover uf2 file](https://cdn.shopify.com/s/files/1/0656/8312/8548/files/midicpPico.uf2)

## Circuitpython Serial Debugging Console

1. Install the [mu editor][https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor]
2. Start the midi captain in fw update mode (switch 0 pressed at boot)
3. with the mu editor, open the boot.py file and the serial consol
4. comment the following lines to enable autoreload
   ```python
   # import supervisor
   # supervisor.disable_autoreload()
   ```
5. Restart in fw update mode. You will see:
   ```shell
   Adafruit CircuitPython 7.3.1 on 2022-06-22; Raspberry Pi Pico with rp2040
   >>>
   ```
6. if you modify the boot.py or the code.py files you will see
   ```shell
   Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
   code.py output:
   ```
7. You can stop the boot pressing `Enter` at the prompt, or soft reboot with `Ctrl+D`


### Relevant Files and Folder Description

based on the [normal+geek_super 3in1 FW4.0](https://cdn.shopify.com/s/files/1/0656/8312/8548/files/FW-MIDICP-10-switch-3in1-V4.0.zip)

```shell
.
├── boot.py                                # Raspbe
├── boot_out.txt
├── code.py                                # Main Python Code
├── lib
│   ├── adafruit_bitmap_font               # Display Libraries
│   ├── adafruit_display_notification
│   ├── adafruit_display_shapes
│   ├── adafruit_display_text
│   ├── adafruit_displayio_layout
│   ├── adafruit_imageload
│   ├── adafruit_progressbar
│   ├── adafruit_st7789.mpy
│   ├── adafruit_framebuf.mpy

│   ├── adafruit_midi                     # Midi Library
│   ├── adafruit_bus_device               #
│   ├── adafruit_hid                      # USB Keyboard
│   ├── adafruit_io                       #
│   ├── adafruit_minimqtt                 # MQTT library?
│   ├── asyncio/                          #
│   ├── adafruit_ticks.mpy                #
│   ├── neopixel.mpy
│   ├── midicaptain.mpy                   # MIDI Captain 
│   ├── midicaptain10s.mpy                # MIDI Captain 
│   ├── midicaptain_ledon.mpy             # MIDI Captain 
│   ├── midigeek.mpy                      # MIDI Captain Geek Mode
│   └── midigeek_C.mpy                    # MIDI Captain 
```

#### boot_out.txt

```
Adafruit CircuitPython 7.3.1 on 2022-06-22; Raspberry Pi Pico with rp2040
Board ID:raspberry_pi_pico
```

#### boot.py

```python
import storage
import board
import digitalio
import time

# remove this two lines to auto reload the code when is modified
import supervisor
supervisor.disable_autoreload()

switch = digitalio.DigitalInOut(board.GP1)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
time.sleep(0.05)

if switch.value is True:
    storage.disable_usb_drive()
    storage.remount("/", readonly=False)
else:
    storage.remount("/", readonly=False)
    m = storage.getmount("/")
    m.label = "MIDICAPTAIN"
    storage.enable_usb_drive()
    storage.remount("/", readonly=True)
```

#### code.py

A lot of code to select the firmware mode.

Pseudocode




# Peripherals

## Midi Captain Blue

The board is based on a Raspberry Pi Core Microcontroller ([Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)),
with the following peripherals:

- 10 footswitches
- 30 RGB led, separately addressables
- Midi In/Out
- 2 expression pedal Input
- Battery
- wireless module 

### GPIO Assignment

| GPIO | PERIPERAL        | PIN FUNCTION |
| ---- | ---------------- | ------------ |
| GP0  | switch           | sw1          |
| GP1  | encoder switch   |              |
| GP2  | encoder A        |              |
| GP3  | encoder B        |              |
| GP4  |                  |              |
| GP5  |                  |              |
| GP6  |                  |              |
| GP7  | _neopixel_       | _neopixel_   |
| GP8  | tft_pwm          |              |
| GP9  | switch           | swA          |
| GP10 | switch           | swB          |
| GP11 | switch           | swC          |
| GP12 | (debug_port??)   |              |
| GP13 | (debug_port??)   |              |
| GP14 |                  | tft_clk? 7   |
| GP15 | (bootsel_pin???) | tft 8        |
| GP16 | uart_midi_tx     |              |
| GP17 | uart_midi_rx     |              |
| GP18 | switch           | swD          |
| GP19 | switch           | swDN         |
| GP20 | switch           | swUP         |
| GP21 |                  |              |
| GP22 |                  |              |
| GP23 | switch           | sw4          |
| GP24 | switch           | sw3          |
| GP25 | switch           | sw2          |
| GP26 |                  |              |
| GP27 |                  |              |
| GP28 |                  |              |
| GP29 |                  |              |

# Reverse engineering code

## Midi UART

### Uart Pins

UART pins can be assigned to any GPIO. default pinout for Raspberry pi pico board:

- UART0:
  | board.GP0 (TX) |
  | b------------) |
- UART1:
  | board.GP4 (TX) |
  | b------------) |

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
```

## Neopixel Led

30 RGB led on the board.

### Test Code

```python
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

```

## Display

Adafruit 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD | ST7789 with EYESPI Connector

- https://www.adafruit.com/product/3787

  1.54" 240x240 Color IPS TFT Display

- https://www.adafruit.com/product/4421

## Pin Assignments

See also: [https://lupyuen.github.io/articles/st7789](https://lupyuen.github.io/articles/st7789)

From [datasheet](https://cdn-shop.adafruit.com/product-files/4421/4421_specs.pdf):

| Pin No. | Symbol    | I/O | Function                                                                                  | Remark |
| ------- | --------- | --- | ----------------------------------------------------------------------------------------- | ------ |
| 1       | LEDA      | P   | LED+                                                                                      |        |
| 2       | LEDK      | P   | LED                                                                                       |        |
| 3       | IM2       | I   |                                                                                           |        |
| 4       | IM1       | I   |                                                                                           |        |
| 5       | IM0       | I   |                                                                                           |        |
| 6       | VCI(2.8V) | P   | Power Supply(2.8V)                                                                        |        |
| 7       | DB7       | I/O | DATA BUS                                                                                  |        |
| 8       | DB6       | I/O | DATA BUS                                                                                  |        |
| 9       | DB5       | I/O | DATA BUS                                                                                  |        |
| 10      | DB4       | I/O | DATA BUS                                                                                  |        |
| 11      | DB3       | I/O | DATA BUS                                                                                  |        |
| 12      | DB2       | I/O | DATA BUS                                                                                  |        |
| 13      | DB1       | I/O | DATA BUS                                                                                  |        |
| 14      | DB0       | I/O | DATA BUS                                                                                  |        |
| 15      | RD        | I   |                                                                                           |        |
| 16      | WR        | I   |                                                                                           |        |
| 17      | RS        | I   |                                                                                           |        |
| 18      | CS        | I   | Chip Selection. Pin-Low Enable.                                                           |        |
| 19      | TE        | O   | Tearing effect output pin to synchronies MCU to frame rate, activated by S/W command.     |        |
| 20      | RESET     | I   | This signal will reset the device and it must be applied to properly initialize the chip. |        |
| 21      | SDA       | I/O | serial input/output signal in serial interface mode.                                      |        |
| 22      | GND       | P   | Ground                                                                                    |        |

## EYESPI Connector

![Eye Pinouts](./images/adafruit_products_EYE_pinouts.jpg?raw=true "EYE Pinouts")

### Pin Description

- Vin: This is the power pin. To power the board (and thus your display), connect
  to the same power as the logic level of your microcontroller, e.g. for a 3V
  micro like a Feather, use 3V, and for a 5V micro like an Arduino, use 5V. |
- Gnd: This is common ground for power and logic.

SPI

- SCK : This is the SPI clock input pin.
- MOSI : This is the SPI MOSI (Microcontroller Out / Serial In) pin. It is used to send data from the microcontroller to the SD card and/or display.
- MISO : This is the SPI MISO (Microcontroller In / Serial Out) pin. It's used for the SD card. It isn't used for the display because it's write-only. It is 3.3V logic out (but can be read by 5V logic).
- DC : This is the display SPI data/command selector pin.
- RST : This is the display reset pin. Connecting to ground resets the display! It's best to have this pin controlled by the library so the display is reset cleanly, but you can also connect it to the Microcontroller's Reset pin, which works for most cases. Often, there is an automatic-reset chip on the display which will reset it on power-up, making this connection unnecessary in that case.
- TCS : This is the TFT or eInk SPI chip select pin.

Backlight Pin

- Lite : This is the PWM input for the backlight control. It is by default pulled high (backlight on), however, you can PWM at any frequency or pull down to turn the backlight off. |

### Wiring

- 3.3V to VIN
- GND to GND
- SCK to SCK clock
- MO to MOSI Seriial Out
- MI to MISO Serial In
- D9 to RST  Reset
- D5 to TCS  Chip select
- LITE backlight pin??

### Pinout

| Pin No. | NAME        | RPI GPIO | Description                    |
| ------- | ----------- |--------- | -------------------------------|
| 1       | GND         |          |                                |
| 2       | PWM         |          |                                |
| 3       | VIN         |          |                                |
| 4       | DATA???     | GPIO12   |                                |
| 5       |             | GPIO16   | RC  network PWM?               |
| 6       | DATA???     | GPIO13   |                                |
| 7       | Inverted?   | GPIO14   |                                |
| 8       | Inverted?   | GPIO15   |                                |

## Wireless Module

### Test code

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
