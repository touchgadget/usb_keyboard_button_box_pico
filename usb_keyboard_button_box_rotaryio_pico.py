# SPDX-License-Identifier: MIT
import time
import board
import digitalio
import rotaryio
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

class Encoder_Keycode():
    Encoders = None

    def __init__(self, encoder_keycode_map):
        self.Encoders = encoder_keycode_map

    def update(self):
        for enc in self.Encoders:
            position = enc["encoder"].position
            last_pos = enc["last_pos"]
            if position > last_pos:
                k = enc["clock_wise"]
                keyboard.press(k)
                time.sleep(0.01)
                keyboard.release(k)
                enc["last_pos"] = position
            elif position < last_pos:
                k = enc["anti_clock_wise"]
                keyboard.press(k)
                time.sleep(0.01)
                keyboard.release(k)
                enc["last_pos"] = position

class Button_Keycode():
    Buttons = None

    def __init__(self, pin_keycode_map):
        self.Buttons = pin_keycode_map
        for btn in self.Buttons:
            pin = digitalio.DigitalInOut(btn["pin"])
            pin.direction = digitalio.Direction.INPUT
            pin.pull = digitalio.Pull.UP
            btn["debouncer"] = Debouncer(pin, interval=0.005)

    def update(self):
        for btn in self.Buttons:
            debounced_pin = btn["debouncer"]
            debounced_pin.update()
            if debounced_pin.fell:
                keyboard.press(btn["keycode"])
            elif debounced_pin.rose:
                keyboard.release(btn["keycode"])

Buttons = Button_Keycode([
    {"pin":board.GP8, "keycode":Keycode.F9},
    {"pin":board.GP9, "keycode":Keycode.F10},
    {"pin":board.GP10, "keycode":Keycode.F11},
    {"pin":board.GP11, "keycode":Keycode.F12},
    {"pin":board.GP12, "keycode":Keycode.F13},
    {"pin":board.GP13, "keycode":Keycode.F14},
    {"pin":board.GP14, "keycode":Keycode.F15},
    {"pin":board.GP16, "keycode":Keycode.F16},
    {"pin":board.GP17, "keycode":Keycode.F17},
    {"pin":board.GP18, "keycode":Keycode.F18},
    {"pin":board.GP19, "keycode":Keycode.F19},
    {"pin":board.GP20, "keycode":Keycode.INSERT},
    {"pin":board.GP21, "keycode":Keycode.DELETE},
    {"pin":board.GP22, "keycode":Keycode.HOME},
    {"pin":board.GP26, "keycode":Keycode.END},
    {"pin":board.GP27, "keycode":Keycode.PAGE_UP},
    {"pin":board.GP28, "keycode":Keycode.PAGE_DOWN},
])

Encoders = Encoder_Keycode([
    {"encoder":rotaryio.IncrementalEncoder(board.GP0, board.GP1), \
        "last_pos":0, "clock_wise":Keycode.F1, "anti_clock_wise":Keycode.F2},
    {"encoder":rotaryio.IncrementalEncoder(board.GP2, board.GP3), \
        "last_pos":0, "clock_wise":Keycode.F3, "anti_clock_wise":Keycode.F4},
    {"encoder":rotaryio.IncrementalEncoder(board.GP4, board.GP5), \
        "last_pos":0, "clock_wise":Keycode.F5, "anti_clock_wise":Keycode.F6},
    {"encoder":rotaryio.IncrementalEncoder(board.GP6, board.GP7), \
        "last_pos":0, "clock_wise":Keycode.F7, "anti_clock_wise":Keycode.F8},
])

while True:
    Encoders.update()
    Buttons.update()
