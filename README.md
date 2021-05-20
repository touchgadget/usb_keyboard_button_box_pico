# USB Keyboard Button Box with Rotary Encoders in CircuitPython

This project creates a USB HID keyboard with 4 rotary encoders and 13 button
inputs. Instead of using keyboard keys, use toggle switches, ignition switches,
etc. to make a car or airplane button box.

## References

### Raspberry Pi Pico and CircuitPython
* https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython

### CircuitPython Libraries
* https://learn.adafruit.com/rotary-encoder
* https://learn.adafruit.com/debouncer-library-python-circuitpython-buttons-sensors/overview
* https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse

Contents of the CIRCUITPY/lib directory. consumer_control\*.mpy and mouse.mpy
could be removed. rotaryio is a built-in library.

```
CIRCUITPY/lib
├── adafruit_debouncer.mpy
└── adafruit_hid
    ├── consumer_control_code.mpy
    ├── consumer_control.mpy
    ├── __init__.mpy
    ├── keyboard_layout_us.mpy
    ├── keyboard.mpy
    ├── keycode.mpy
    └── mouse.mpy
```

## Hardware

### Board running CircuitPython 6.2.

In this example, the Raspberry Pi Pico is used because it exposes many GPIO
pins on a $4 board. Other boards running CircuitPython can be used but the
number of pins and the names of pins must be changed.

### Rotary Encoders

Note: This project uses 5 pin rotary encoders. KY-040 rotary encoder boards
should work. It does not use Adafruit's Seesaw Rotary Encoder I2C boards.

Each rotary encoder has 3 pins on one side and 2 pins on the other. The 2 pins
are ground and button output. The 3 pins are ground, A, and B.

## Connections

The following table shows 4 rotary encoders are connected to a Raspberry Pi
Pico board. The remaining pins are configured for button inputs.

The pin label refers the white text printed on back of the Pico. The
CircuitPython (CP) pin name refers to the same pin but is the name used in CP
programs.

0.A refers to rotary encoder 0 pin A and similarly for 0.B. 0.button refers to
the button output pin. Note there are two pins for the button. One must be
connected to ground and the other is the button output pin. It does not matter
which is which. However, this is not true for the A and B pins. Swapping them
reverses the direction of rotation so if an encoder behaves backwards, swapping
the A and B pins should fix it.

Rotary Encoder  |Pico pin label |CP pin name
----------------|---------------|----------------
0.A             |GP0            |board.GP0
0.B             |GP1            |board.GP1
0.button        |GP8            |board.GP8
0.GND           |GND            |
1.A             |GP2            |board.GP2
1.B             |GP3            |board.GP3
1.button        |GP9            |board.GP9
1.GND           |GND            |
2.A             |GP4            |board.GP4
2.B             |GP5            |board.GP5
2.button        |GP10           |board.GP10
2.GND           |GND            |
3.A             |GP6            |board.GP6
3.B             |GP7            |board.GP7
3.button        |GP11           |board.GP11
3.GND           |GND            |

The remaining pins are handled as normally open push buttons. Each button must
also have one its terminals connected to a Pico ground (GND).

Plain Button    |Pico pin label |CP pin name
----------------|---------------|----------------
B1              |GP12           |board.GP12
B2              |GP13           |board.GP13
B3              |GP14           |board.GP14
B4              |GP16           |board.GP16
B5              |GP17           |board.GP17
B6              |GP18           |board.GP18
B7              |GP19           |board.GP19
B8              |GP20           |board.GP20
B9              |GP21           |board.GP21
B10             |GP22           |board.GP22
B11             |GP26_A0        |board.GP26
B12             |GP27_A1        |board.GP27
B13             |GP28_A2        |board.GP28

The following table shows the USB keys sent by the Pico.

USB Key  |Action
---------|-----------------
F1       |Rotary encoder 0 clock wise rotation
F2       |Rotary encoder 0 counter clock wise rotation
F3       |Rotary encoder 1 clock wise rotation
F4       |Rotary encoder 1 counter clock wise rotation
F5       |Rotary encoder 2 clock wise rotation
F6       |Rotary encoder 2 counter clock wise rotation
F7       |Rotary encoder 3 clock wise rotation
F8       |Rotary encoder 3 counter clock wise rotation
F9       |Rotary encoder 0 button
F10      |Rotary encoder 1 button
F11      |Rotary encoder 2 button
F12      |Rotary encoder 3 button
F13      |Button 1
F14	     |Button 2
F15	     |Button 3
F16	     |Button 4
F17	     |Button 5
F18	     |Button 6
F19	     |Button 7
INSERT   |Button 8
DELETE   |Button 9
HOME     |Button 10
END	     |Button 11
PAGE_UP  |Button 12
PAGE_DOWN|Button 13
