import asyncio
import board
import asyncio
import busio
import digitalio
# import usb_midi
import neopixel
import adafruit_midi
import time

from adafruit_midi.control_change import ControlChange
from adafruit_midi.midi_message import MIDIUnknownEvent
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.system_exclusive import SystemExclusive
from adafruit_midi.timing_clock import TimingClock

# Define MIDI channel (0-15)
midi_channel = 0

# Create a UART object for TX and RX pins (modify if different)
uart = busio.UART(tx=board.GP16, rx=board.GP17, baudrate=31250, timeout=0.2001)  # Adjust baudrate if needed
pixels = neopixel.NeoPixel(board.GP7, 30, auto_write=False)

# Create a MIDI object using the UART
sermidi = adafruit_midi.MIDI(midi_in=uart, midi_out=uart, out_channel=0)

def set_led_color(index, color):
    idx_zero = index * 3
    pixels.fill((0,0,0))
    pixels[idx_zero] = pixels[idx_zero + 1] = pixels[idx_zero + 2] = color
    pixels.show()

def led_off():
    pixels.fill((0,0,0))
    pixels.show()

def midi_message_to_str(msg):
    if isinstance(msg, NoteOn):
        return f"NOTE ON [{msg.channel}][{msg.note}][{msg.velocity}]"
    elif isinstance(msg, NoteOff):
        return f"NOTE OFF [{msg.channel}][{msg.note}][{msg.velocity}]"
    elif isinstance(msg, ProgramChange):
        return f"PC [{msg.channel}][{msg.patch}]"
    elif isinstance(msg, ControlChange):
        return f"CC [{msg.channel}][{msg.control}][{msg.value}]"
    else:
        return f"Unknown MIDI message = {msg}"

async def receive_midi_messages():
    while True:
        msg = sermidi.receive()
        if msg is not None:
            print("Received midi msg =", midi_message_to_str(msg))  # Print the received MIDI message
        await asyncio.sleep(0.1)  # Small delay to avoid overwhelming output

async def midi_cc_send():
    while True:
        print("Send CC 0 127")
        sermidi.send(ControlChange(control=0, value=127))
        set_led_color(9, (100, 100, 0))
        await asyncio.sleep(1)

        print("Send CC 0 0")
        sermidi.send(ControlChange(control=0, value=0))
        led_off()
        await asyncio.sleep(1)

        print("Send PC 1 1")
        sermidi.send(ProgramChange(patch=1))
        set_led_color(9, (255, 255, 0))
        await asyncio.sleep(1)

        print("Send Note On")
        sermidi.send(NoteOn(note=34, velocity=124))
        set_led_color(9, (0, 255, 255))
        await asyncio.sleep(1)

        print("Send Note Off")
        sermidi.send(NoteOff(note=34))
        set_led_color(9, (0, 255, 0))
        await asyncio.sleep(1)


async def main():
    """Main function to run asynchronous tasks"""
    midi_cc_send_task = asyncio.create_task(midi_cc_send())
    receive_midi_messages_task = asyncio.create_task(receive_midi_messages())
    await asyncio.gather(midi_cc_send_task, receive_midi_messages_task)

# start the main coroutine
asyncio.run(main())
