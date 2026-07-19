# ---> Standard library imports <--- #
from typing import Literal, get_args

# ---> Local imports <--- #
from .types import (
  ClearActionNameType,
  ColorNameType,
  CursorActionNameType,
  CursorActionsThatHaveNoNumberParametersNameType,
  CursorActionsThatHaveOneNumberParameterNameType,
  CursorActionsThatHaveTwoNumberParametersNameType,
  FormatNameType,
)


COLOR_CODES: dict[Literal["foreground", "background"], dict[ColorNameType, int]] = {
  "foreground": {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "default": 39,
    "bright_black": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97
  },
  "background": {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47,
    "default": 49,
    "bright_black": 100,
    "bright_red": 101,
    "bright_green": 102,
    "bright_yellow": 103,
    "bright_blue": 104,
    "bright_magenta": 105,
    "bright_cyan": 106,
    "bright_white": 107
  }
}


FORMAT_CODES: dict[Literal["apply", "reset"], dict[FormatNameType, int]] = {
  "apply": {
    "bold": 1,
    "dim": 2,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "swap_colors": 7,
    "hidden": 8,
    "strikethrough": 9
  },
  "reset": {
    "bold": 21,
    "dim": 22,
    "italic": 23,
    "underline": 24,
    "blink": 25,
    "swap_colors": 27,
    "hidden": 28,
    "strikethrough": 29
  }
}


CURSOR_CODES: dict[CursorActionNameType, str] = {
  "up": "A",                    "u": "A",
  "down": "B",                  "d": "B",
  "forward": "C",               "f": "C",
  "backward": "D",              "b": "D",
  "start_of_line_down": "E",    "sold": "E",
  "start_of_line_up": "F",      "solu": "F",
  "move_to_column": "G",        "mtc": "G",
  "move_to_position": "H",      "mtp": "H",
  "save_position": "s",         "sp": "s",
  "restore_position": "u",      "rp": "u",
  "hide": "?25l",               "h": "?25l",
  "show": "?25h",               "s": "?25h"
}


CLEAR_CODES: dict[ClearActionNameType, str] = {
  "all": "2J",                  "a": "2J",
  "begin_to_cursor": "1J",      "btc": "1J",
  "cursor_to_end": "0J",        "cte": "0J",
  "line": "2K",                 "l": "2K",
  "line_start_to_cursor": "1K", "lstc": "1K",
  "cursor_to_line_end": "0K",   "ctle": "0K"
}


COLOR_NAMES: tuple[ColorNameType, ...] = get_args(ColorNameType.__value__)

CURSOR_ACTIONS_THAT_HAVE_ONE_NUMBER_PARAMETER: tuple[CursorActionsThatHaveOneNumberParameterNameType, ...] = (
  get_args(CursorActionsThatHaveOneNumberParameterNameType.__value__)
)
CURSOR_ACTIONS_THAT_HAVE_TWO_NUMBER_PARAMETERS: tuple[CursorActionsThatHaveTwoNumberParametersNameType, ...] = (
  get_args(CursorActionsThatHaveTwoNumberParametersNameType.__value__)
)
CURSOR_ACTIONS_THAT_HAVE_NO_NUMBER_PARAMETERS: tuple[CursorActionsThatHaveNoNumberParametersNameType, ...] = (
  get_args(CursorActionsThatHaveNoNumberParametersNameType.__value__)
)
