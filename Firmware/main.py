import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.macros import Macros  # Required for typing out text strings


keyboard = KMKKeyboard()


# We need to add this module so the keyboard knows how to type full sentencesssssss.
macros = Macros()
keyboard.modules.append(macros)


# These are the actual pins on the Pico (GP0, GP1, etc.)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)


# This tells the code which way the electricity flows through the switches.
# If the keys aren't working at all. then like probably try changing this to ROW2COL.
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# This is the layout of the 3x3 pad.
# I've switched the shortcuts (Copy/Paste) to a cleaner syntax.
keyboard.keymap = [
    # Row 0
    [
        KC.MACRO("I hate kittens."),   # SW1: Types this phrase exactly.
        KC.LCTRL(KC.S),                # SW4: Save (Ctrl + S)
        KC.RGB_TOG,                    # SW7: Turn the LEDs on or off
    ],

    # Row 1
    [
        KC.MACRO("youremail@example.com"), # SW2: Types your email
        KC.LCTRL(KC.C),                    # SW5: Copy (Ctrl + C)
        KC.LCTRL(KC.V),                    # SW8: Paste (Ctrl + V)
    ],

    # Row 2
    [
        KC.KP_7,                       # SW3: Number pad 7
        KC.LCTRL(KC.X),                # SW6: Cut (Ctrl + X)
        KC.KP_9,                       # SW9: Number pad 9
    ],
]


# This controls the underglow or per-key LEDs.
rgb = RGB(
    pixel_pin=board.GP3,        # The pin where the LED data wire is connected
    num_pixels=12,              # Total number of LEDs on the strip/board
    val_limit=150,              # Safety limit: Max brightness (0-255). 255 is blinding but its betiful ｡◕‿‿◕｡!
    val_default=100,            # Starting brightness
    animation_speed=1,
    animation_mode=AnimationModes.RAINBOW,
    # IMPORTANT: The line below is for RGBW (Red, Green, Blue, White) LEDs.
    # If your colors look wrong (like Green is Red), change this to (1, 0, 2)
    rgb_order=(1, 0, 2, 3), 
)

keyboard.extensions.append(rgb)


if __name__ == "__main__":
    keyboard.go()
# ¬_¬