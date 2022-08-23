# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_hid.keycode.Keycode`
====================================================

* Author(s): Scott Shawcroft, Dan Halbert
* Custemed by koyaaaaaan
"""


class Keycode:
    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1A
    X = 0x1B
    Y = 0x1C
    Z = 0x1D

    ONE = 0x1E
    TWO = 0x1F
    THREE = 0x20
    FOUR = 0x21
    FIVE = 0x22
    SIX = 0x23
    SEVEN = 0x24
    EIGHT = 0x25
    NINE = 0x26
    ZERO = 0x27
    ENTER = 0x28
    RETURN = ENTER
    ESCAPE = 0x29
    BACKSPACE = 0x2A
    TAB = 0x2B
    SPACEBAR = 0x2C
    SPACE = SPACEBAR
    ATSIGN = 0x13
    MINUS = 0x2D
    HAT = 0x2e
    LEFT_BRACKET = 0x2F
    RIGHT_BRACKET = 0x30
    BACKSLASH = 0x31
    POUND = 0x32
    COLON = 0x34
    SEMICOLON = 0x33
    GRAVE_ACCENT = 0x35 # かな/英数変換キー
    COMMA = 0x36
    PERIOD = 0x37
    FORWARD_SLASH = 0x38

    CAPS_LOCK = 0x39

    F1 = 0x3A
    F2 = 0x3B
    F3 = 0x3C
    F4 = 0x3D
    F5 = 0x3E
    F6 = 0x3F
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45

    PRINT_SCREEN = 0x46
    SCROLL_LOCK = 0x47
    PAUSE = 0x48

    INSERT = 0x49
    HOME = 0x4A
    PAGE_UP = 0x4B
    DELETE = 0x4C
    END = 0x4D
    PAGE_DOWN = 0x4E

    RIGHT_ARROW = 0x4F
    LEFT_ARROW = 0x50
    DOWN_ARROW = 0x51
    UP_ARROW = 0x52

    KEYPAD_NUMLOCK = 0x53
    KEYPAD_FORWARD_SLASH = 0x54
    KEYPAD_ASTERISK = 0x55
    KEYPAD_MINUS = 0x56
    KEYPAD_PLUS = 0x57
    KEYPAD_ENTER = 0x58
    KEYPAD_ONE = 0x59
    KEYPAD_TWO = 0x5A
    KEYPAD_THREE = 0x5B
    KEYPAD_FOUR = 0x5C
    KEYPAD_FIVE = 0x5D
    KEYPAD_SIX = 0x5E
    KEYPAD_SEVEN = 0x5F
    KEYPAD_EIGHT = 0x60
    KEYPAD_NINE = 0x61
    KEYPAD_ZERO = 0x62
    KEYPAD_PERIOD = 0x63
    KEYPAD_BACKSLASH = 0x64

    # For Mac ----
    APPLICATION = 0x65
    POWER = 0x66
    KEYPAD_EQUALS = 0x67
    F13 = 0x68
    F14 = 0x69
    F15 = 0x6A
    F16 = 0x6B
    F17 = 0x6C
    F18 = 0x6D
    F19 = 0x6E
    F20 = 0x6F
    F21 = 0x70
    F22 = 0x71
    F23 = 0x72
    F24 = 0x73
    # End for Mac ----

    LEFT_CONTROL = 0xE0
    CONTROL = LEFT_CONTROL
    LEFT_SHIFT = 0xE1
    SHIFT = LEFT_SHIFT
    LEFT_ALT = 0xE2
    ALT = LEFT_ALT
    OPTION = ALT
    LEFT_GUI = 0xE3
    GUI = LEFT_GUI
    WINDOWS = GUI
    COMMAND = GUI
    RIGHT_CONTROL = 0xE4
    RIGHT_SHIFT = 0xE5
    RIGHT_ALT = 0xE6
    RIGHT_GUI = 0xE7
    """\ or _ in JP"""
    INTERNATIONAL1 = 0x87
    """ひらがな カタカナ in JP"""
    INTERNATIONAL2 = 0x87
    """¥ or | in JP"""
    INTERNATIONAL3 = 0x87
    """変換 in JP"""
    INTERNATIONAL4 = 0x87
    """無変換 in JP"""
    INTERNATIONAL5 = 0x87


    # pylint: enable-msg=invalid-name
    @classmethod
    def modifier_bit(cls, keycode):
        try:
            return (
                1 << (keycode - 0xE0) if cls.LEFT_CONTROL <= keycode <= cls.RIGHT_GUI else 0
            )
        except:
            return false
