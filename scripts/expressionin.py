# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn

exp1 = AnalogIn(board.A1)
exp2 = AnalogIn(board.A2)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    print("EXP1=", get_voltage(exp1), " EXP2=", get_voltage(exp2))
    time.sleep(0.1)
