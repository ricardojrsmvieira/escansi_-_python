"""
Types module for the escansi package.

This module defines types for ANSI escape codes, including:
- Color names;
- Format names;
- Cursor actions names;
- Clear actions names.
"""

# ---> Standard library imports <--- #
from typing import Literal


type ColorNameType = Literal[
  'black',
  'red',
  'green',
  'yellow',
  'blue',
  'magenta',
  'cyan',
  'white',
  'default',
  'bright_black',
  'bright_red',
  'bright_green',
  'bright_yellow',
  'bright_blue',
  'bright_magenta',
  'bright_cyan',
  'bright_white'
]


type FormatNameType = Literal[
  'bold',
  'dim',
  'italic',
  'underline',
  'blink',
  'swap_colors',
  'hidden',
  'strikethrough'
]


# THIS TYPES ARE RELATED ->
#   If need to add/remove to the first one (main), consider where else it should be added/removed
#   to keep the consistency.
type CursorActionNameType = Literal[
  # CursorActionsThatHaveOneNumberParameterNameType
  'up',                   'u',
  'down',                 'd',
  'forward',              'f',
  'backward',             'b',
  'start_of_line_down',   'sold',
  'start_of_line_up',     'solu',
  'move_to_column',       'mtc',
  # CursorActionsThatHaveTwoNumberParametersNameType
  'move_to_position',     'mtp',
  # CursorActionsThatHaveNoNumberParametersNameType
  'save_position',        'sp',
  'restore_position',     'rp',
  'hide',                 'h',
  'show',                 's'
]

type CursorActionsThatHaveOneNumberParameterNameType = Literal[
  'up',                   'u',
  'down',                 'd',
  'forward',              'f',
  'backward',             'b',
  'start_of_line_down',   'sold',
  'start_of_line_up',     'solu',
  'move_to_column',       'mtc'
]

type CursorActionsThatHaveTwoNumberParametersNameType = Literal[
  'move_to_position',     'mtp'
]

type CursorActionsThatHaveNoNumberParametersNameType = Literal[
  'save_position',        'sp',
  'restore_position',     'rp',
  'hide',                 'h',
  'show',                 's'
]
# <- THIS TYPES ARE RELATED


type ClearActionNameType = Literal[
  'all',                  'a',
  'begin_to_cursor',      'btc',
  'cursor_to_end',        'cte',
  'line',                 'l',
  'line_start_to_cursor', 'lstc',
  'cursor_to_line_end',   'ctle'
]
