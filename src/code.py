import board
import time
import digitalio

switch2 = digitalio.DigitalInOut(board.GP25)
switch2.direction = digitalio.Direction.INPUT
switch2.pull = digitalio.Pull.UP

switch3 = digitalio.DigitalInOut(board.GP24)
switch3.direction = digitalio.Direction.INPUT
switch3.pull = digitalio.Pull.UP

switch4 = digitalio.DigitalInOut(board.GP23)
switch4.direction = digitalio.Direction.INPUT
switch4.pull = digitalio.Pull.UP

switchUp = digitalio.DigitalInOut(board.GP20)
switchUp.direction = digitalio.Direction.INPUT
switchUp.pull = digitalio.Pull.UP

switchA = digitalio.DigitalInOut(board.GP9)
switchA.direction = digitalio.Direction.INPUT
switchA.pull = digitalio.Pull.UP

switchB = digitalio.DigitalInOut(board.GP10)
switchB.direction = digitalio.Direction.INPUT
switchB.pull = digitalio.Pull.UP

switchC = digitalio.DigitalInOut(board.GP11)
switchC.direction = digitalio.Direction.INPUT
switchC.pull = digitalio.Pull.UP

switchD = digitalio.DigitalInOut(board.GP18)
switchD.direction = digitalio.Direction.INPUT
switchD.pull = digitalio.Pull.UP

switchDown = digitalio.DigitalInOut(board.GP19)
switchDown.direction = digitalio.Direction.INPUT
switchDown.pull = digitalio.Pull.UP
time.sleep(0.05)

firmware_ID = 1

if switch2.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 2

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switch3.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 3

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switch4.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 4

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchUp.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 5

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchA.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 6

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchB.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 7

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchC.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 8

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchD.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 9

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

elif switchDown.value is False:

    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

    firmware_ID = 10

    try:
        with open('/res/firmwareid.dat', "r+") as fp4:
            for line2 in fp4:
                if line2.find('FIRMWARE_ID') != (-1):
                    value_bytes = line2[line2.find('['):line2.find(']') + 1]
                    temp_str = '[' + str(firmware_ID) + ']'
                    line3 = line2.replace(value_bytes, temp_str)
                    line4 = line3[0:105]
                    fp4.seek(-len(line2), 1)
                    fp4.write(line4)
    except OSError:
        print('error write files')
        pass

else:
    switch2.deinit()
    switch3.deinit()
    switch4.deinit()
    switchUp.deinit()
    switchA.deinit()
    switchB.deinit()
    switchC.deinit()
    switchD.deinit()
    switchDown.deinit()

try:
    with open('/res/firmwareid.dat', 'r') as fp:
        fm_id = fp.read()
        for line in fm_id.split('\n'):
            linedata = line.replace(' ', '')
            itemdata = linedata[0:linedata.find('=')]
            valuedata = linedata[linedata.find('[') + 1:linedata.find(']')]
            if itemdata == 'FIRMWARE_ID':
                firmware_ID = int(valuedata)
                if firmware_ID < 1 or firmware_ID > 10:
                    firmware_ID = 1

except OSError:
    print('error open')
    firmware_ID = 1
    pass

del switch2
del switch3
del switch4
del switchA
del switchB
del switchC
del switchD
del switchUp
del switchDown

if firmware_ID == 1:
   import midicaptain
elif firmware_ID == 6:
   import midicaptain
elif firmware_ID == 2:
   import midigeek
elif firmware_ID == 7:
   import midicaptain_ledon
elif firmware_ID == 3:
   import midigeek_C
elif firmware_ID == 8:
   import midicaptain10s
elif firmware_ID == 4:
   import midigeek
elif firmware_ID == 9:
   import midicaptain
elif firmware_ID == 5:
   import midigeek
elif firmware_ID == 10:
   import midicaptain
else:
    import midicaptain
