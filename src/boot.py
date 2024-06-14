import board
import digitalio
import storage
import time

# import supervisor
# supervisor.disable_autoreload()

switch = digitalio.DigitalInOut(board.GP1)  # change for the final product
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

switch.deinit()
