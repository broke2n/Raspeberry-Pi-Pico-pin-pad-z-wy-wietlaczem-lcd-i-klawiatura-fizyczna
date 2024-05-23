import board
import busio
import time
import digitalio
import adafruit_matrixkeypad
import random
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import terminalio

displayio.release_displays()

spi = busio.SPI(clock=board.GP18, MOSI=board.GP19)
dc = board.GP21
cs = board.GP17
reset = board.GP20

display_bus = displayio.FourWire(spi, command=dc, chip_select=cs, reset=reset)

WIDTH = 128
HEIGHT = 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

def disOLED(row0,row1,row2,row3,row4,row5):
    text_0 = "Input:	{}".format(row0)
    text_1 = '|'.join(map(str,row1))
    text_2 = '|'.join(map(str,row2))
    text_3 = '|'.join(map(str,row3))
    text_4 = '|'.join(map(str,row4))
    text_5 = '|'.join(map(str,row5))
    

    y_start_positions = [8,20,30,40,50,60]

    text_area_0 = label.Label(terminalio.FONT, text=text_0, color=0xFFFF00, x= 0,y=y_start_positions[0])
    text_area_1 = label.Label(terminalio.FONT, text=text_1, color=0xFFFF00, x= 0,y=y_start_positions[1])
    text_area_2 = label.Label(terminalio.FONT, text=text_2, color=0xFFFF00, x= 0,y=y_start_positions[2])
    text_area_3 = label.Label(terminalio.FONT, text=text_3, color=0xFFFF00, x= 0,y=y_start_positions[3])
    text_area_4 = label.Label(terminalio.FONT, text=text_4, color=0xFFFF00, x= 0,y=y_start_positions[4])
    text_area_5 = label.Label(terminalio.FONT, text=text_5, color=0xFFFF00, x= 0,y=y_start_positions[5])
    splash = displayio.Group()
    splash.append(text_area_0)
    splash.append(text_area_1)
    splash.append(text_area_2)
    splash.append(text_area_3)
    splash.append(text_area_4)
    splash.append(text_area_5)

    display.root_group = splash
    
def disOLED2(row0,row1,row2,row3,row4,row5):
    text_0 = "Input:	{}".format(row0)
    text_1 = ''.join(map(str,row1))
    text_2 = ''.join(map(str,row2))
    text_3 = ''.join(map(str,row3))
    text_4 = ''.join(map(str,row4))
    text_5 = ''.join(map(str,row5))
    

    y_start_positions = [8,20,30,40,50,60]

    text_area_0 = label.Label(terminalio.FONT, text=text_0, color=0xFFFF00, x= 0,y=y_start_positions[0])
    text_area_1 = label.Label(terminalio.FONT, text=text_1, color=0xFFFF00, x= 0,y=y_start_positions[1])
    text_area_2 = label.Label(terminalio.FONT, text=text_2, color=0xFFFF00, x= 0,y=y_start_positions[2])
    text_area_3 = label.Label(terminalio.FONT, text=text_3, color=0xFFFF00, x= 0,y=y_start_positions[3])
    text_area_4 = label.Label(terminalio.FONT, text=text_4, color=0xFFFF00, x= 0,y=y_start_positions[4])
    text_area_5 = label.Label(terminalio.FONT, text=text_5, color=0xFFFF00, x= 0,y=y_start_positions[5])
    splash = displayio.Group()
    splash.append(text_area_0)
    splash.append(text_area_1)
    splash.append(text_area_2)
    splash.append(text_area_3)
    splash.append(text_area_4)
    splash.append(text_area_5)

    display.root_group = splash
    
password = ""
keyValues = ["A","B","C","D","1","2","3","E","4","5","6","F","7","8","9","@","*","0","#","!"]
randomValues = []

    
cols = [digitalio.DigitalInOut(pin) for pin in (board.GP0, board.GP1, board.GP2, board.GP3)]
rows = [digitalio.DigitalInOut(pin) for pin in (board.GP8, board.GP7, board.GP6, board.GP5, board.GP4)]

def randomKeyboard():
    global key1
    while keyValues:
        element = random.choice(keyValues)
        randomValues.append(element)
        keyValues.remove(element)
    
        key1 = [randomValues[i:i+4] for i in range(0, len(randomValues), 4)]

def normalKeyboard():
    global keys
    keys = [keyValues[i:i+4] for i in range(0, len(keyValues), 4)]

def discOUTPUT(n):
    global string
    string = (n * "* " + "- " *(5-n))

inout = 0
inputedPassword = ''
inputedChars = []
decision = []
d = ''

while inout == 0 and password == '':
    normalKeyboard()
    keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
    key = keypad.pressed_keys
    if key and (len(inputedChars) <=5):
        inputedChars.append(key)
        inputedPassword = ''.join(''.join(char for char in string if char != ('[' or "'" or ']')) for string in inputedChars)
    if (len(inputedChars) <=5): disOLED(inputedPassword,keys[0],keys[1],keys[2],keys[3],keys[4])
    if len(inputedPassword) == 5:
        inputedChars = []
        password = inputedPassword
        inputedPassword = ''
    time.sleep(0.1)
    
while inout == 0 and password != '':
    discOUTPUT(len(inputedChars))
    randomKeyboard()
    keypad2 = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, key1)
    if len(inputedChars)<=5: disOLED(inputedPassword,key1[0],key1[1],key1[2],key1[3],key1[4])
    key = keypad2.pressed_keys
    if key and len(inputedChars)<=5:
        inputedChars.append(key)
        inputedPassword = ''.join(''.join(char for char in string if char != ('[' or "'" or ']')) for string in inputedChars)
    if len(inputedPassword) == 5:
        if(inputedPassword == password):
            inout = 1
        else:
            inputedPassword = ''
            inputedChars = []
            
while inout == 1:
    disOLED2("","PASSWORD","IS","CORRECT","",":)")




