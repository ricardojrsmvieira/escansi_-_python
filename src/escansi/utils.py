"""
Utilities module for the escansi package.

This module defines utility functions for ANSI escape codes, including:
- fore_color();
- back_color();
- format_text();
- reset_formats();
- cursor();
- clear().
"""

# ---> Standard library imports <--- #
from typing import Literal, overload

# ---> Local imports <--- #
from .constants import (
  CLEAR_CODES,
  COLOR_CODES,
  COLOR_NAMES,
  CURSOR_ACTIONS_THAT_HAVE_NO_NUMBER_PARAMETERS,
  CURSOR_ACTIONS_THAT_HAVE_ONE_NUMBER_PARAMETER,
  CURSOR_ACTIONS_THAT_HAVE_TWO_NUMBER_PARAMETERS,
  CURSOR_CODES,
  FORMAT_CODES,
)
from .types import (
  ClearActionNameType,
  CursorActionNameType,
  CursorActionsThatHaveNoNumberParametersNameType,
  CursorActionsThatHaveOneNumberParameterNameType,
  CursorActionsThatHaveTwoNumberParametersNameType,
  FormatNameType,
)


#region overloads
@overload
def fore_color(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: None = None,
  blue: None = None,
  /
) -> str: ...
@overload
def fore_color(
  color_or_grey_or_red: int,
  green: int,
  blue: int,
  /
) -> str: ...
#endregion overloads
def fore_color(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: int | None = None,
  blue: int | None = None,
  /
) -> str:
  """
  Get the ANSI escape code for the specified foreground color.

  Parameters
  ----------
  color_or_grey_or_red : str | int | tuple[int, int, int]
      The foreground color specified as a color name, 8-bit color code, or RGB tuple.
      Can also correspond to the red component of an RGB color if green and blue are provided.
  green : int | None,, default None
      The green component of the RGB color. Defaults to None.
  blue : int | None,, default None
      The blue component of the RGB color. Defaults to None.

  Raises
  ------
  ValueError :
      If the color code or name is invalid.

  Returns
  -------
  str :
      The ANSI escape code for the specified foreground color.

  Examples
  --------
  >>> fore_color('green')
  >>> fore_color('#FF00AA')
  >>> fore_color(123)
  >>> fore_color(255, 0, 170)
  >>> fore_color((255, 0, 170))
  """
  if isinstance(color_or_grey_or_red, str):
    if color_or_grey_or_red in COLOR_NAMES:
      return f"\033[{COLOR_CODES['foreground'][color_or_grey_or_red]}m"
    if color_or_grey_or_red.startswith('#') and len(color_or_grey_or_red) == 7:  # noqa: PLR2004
      try:
        r = int(color_or_grey_or_red[1:3], 16)
        g = int(color_or_grey_or_red[3:5], 16)
        b = int(color_or_grey_or_red[5:7], 16)
      except ValueError as e:
        msg = f"Invalid color code or name: '{color_or_grey_or_red}'"
        raise ValueError(msg) from e
      else:
        return f'\033[38;2;{r};{g};{b}m'
    else:
      msg = f"Invalid color code or name: '{color_or_grey_or_red}'"
      raise ValueError(msg)
  elif green is None or blue is None:
    if isinstance(color_or_grey_or_red, tuple):
      r, g, b = color_or_grey_or_red
      return f'\033[38;2;{r};{g};{b}m'
    return f'\033[38;5;{color_or_grey_or_red}m'
  else:
    return f'\033[38;2;{color_or_grey_or_red};{green};{blue}m'


#region overloads
@overload
def back_color(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: None = None,
  blue: None = None,
  /
) -> str: ...
@overload
def back_color(
  color_or_grey_or_red: int,
  green: int,
  blue: int,
  /
) -> str: ...
#endregion overloads
def back_color(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: int | None = None,
  blue: int | None = None,
  /
) -> str:
  """
  Get the ANSI escape code for the specified background color.

  Parameters
  ----------
  color_or_grey_or_red : str | int | tuple[int, int, int]
      The background color specified as a color name, 8-bit color code, or RGB tuple.
      Can also correspond to the red component of an RGB color if green and blue are provided.
  green : int | None,, default None
      The green component of the RGB color. Defaults to None.
  blue : int | None,, default None
      The blue component of the RGB color. Defaults to None.

  Raises
  ------
  ValueError :
      If the color code or name is invalid.

  Returns
  -------
  str :
      The ANSI escape code for the specified background color.

  Examples
  --------
  >>> back_color('green')
  >>> back_color('#FF00AA')
  >>> back_color(123)
  >>> back_color(255, 0, 170)
  >>> back_color((255, 0, 170))
  """
  if isinstance(color_or_grey_or_red, str):
    if color_or_grey_or_red in COLOR_NAMES:
      return f"\033[{COLOR_CODES['background'][color_or_grey_or_red]}m"
    if color_or_grey_or_red.startswith('#') and len(color_or_grey_or_red) == 7:  # noqa: PLR2004
      try:
        r = int(color_or_grey_or_red[1:3], 16)
        g = int(color_or_grey_or_red[3:5], 16)
        b = int(color_or_grey_or_red[5:7], 16)
      except ValueError as e:
        msg = f"Invalid color code or name: '{color_or_grey_or_red}'"
        raise ValueError(msg) from e
      else:
        return f'\033[48;2;{r};{g};{b}m'
    else:
      msg = f"Invalid color code or name: '{color_or_grey_or_red}'"
      raise ValueError(msg)
  elif green is None or blue is None:
    if isinstance(color_or_grey_or_red, tuple):
      r, g, b = color_or_grey_or_red
      return f'\033[48;2;{r};{g};{b}m'
    return f'\033[48;5;{color_or_grey_or_red}m'
  else:
    return f'\033[48;2;{color_or_grey_or_red};{green};{blue}m'


def format_text(formats: FormatNameType | tuple[FormatNameType, ...]) -> str:
  """
  Get the ANSI escape code for the specified text format.

  Parameters
  ----------
  formats : FormatNameType | tuple[FormatNameType, ...]
      The text format(s) to apply.

  Returns
  -------
  str :
      The ANSI escape code for the specified text format(s).

  Examples
  --------
  >>> format_text('bold')
  >>> format_text(('bold', 'underline'))
  """
  if isinstance(formats, tuple):
    return ''.join(f"\033[{FORMAT_CODES['apply'][f]}m" for f in formats)
  return f"\033[{FORMAT_CODES['apply'][formats]}m"


def reset_formats(
  formats: FormatNameType | tuple[FormatNameType, ...] | Literal['all'] = 'all'
) -> str:
  """
  Get the ANSI escape code to reset the specified text format(s).

  Parameters
  ----------
  formats : FormatNameType | tuple[FormatNameType, ...] | 'all',, default 'all'
      The text format(s) to reset. If 'all', resets all.

  Returns
  -------
  str :
      The ANSI escape code to reset the specified text format(s).

  Examples
  --------
  >>> reset_formats()
  >>> reset_formats('all')
  >>> reset_formats('bold')
  >>> reset_formats(('bold', 'underline'))
  """
  if formats == 'all':
    return '\033[0m'
  if isinstance(formats, tuple):
    return ''.join(f"\033[{FORMAT_CODES['reset'][f]}m" for f in formats)
  return f"\033[{FORMAT_CODES['reset'][formats]}m"


#region overloads
@overload
def cursor(
action: CursorActionsThatHaveNoNumberParametersNameType,
  n: None = None,
  m: None = None,
  /
) -> str: ...
@overload
def cursor(
action: CursorActionsThatHaveOneNumberParameterNameType,
  n: int,
  m: None = None,
  /
) -> str: ...
@overload
def cursor(
action: CursorActionsThatHaveTwoNumberParametersNameType,
  n: int,
  m: int,
  /
) -> str: ...
#endregion overloads
def cursor(
  action: CursorActionNameType,
  n: int | None = None,
  m: int | None = None,
  /
) -> str:
  """
  Get the ANSI escape code for the specified cursor action.

  Parameters
  ----------
  action : CursorActionNameType
      The cursor action to perform.
  n : int | None,, default None
      The first numeric parameter for the cursor action, if applicable.
  m : int | None,, default None
      The second numeric parameter for the cursor action, if applicable.

  Raises
  ------
  ValueError :
      If the cursor action is invalid.

  Returns
  -------
  str :
      The ANSI escape code for the specified cursor action.

  Examples
  --------
  >>> cursor('show')
  >>> cursor('up', 3)
  >>> cursor('move_to_position', 5, 10)
  """
  if action in CURSOR_ACTIONS_THAT_HAVE_ONE_NUMBER_PARAMETER:
    return f'\033[{n}{CURSOR_CODES[action]}'
  if action in CURSOR_ACTIONS_THAT_HAVE_TWO_NUMBER_PARAMETERS:
    return f'\033[{n};{m}{CURSOR_CODES[action]}'
  if action in CURSOR_ACTIONS_THAT_HAVE_NO_NUMBER_PARAMETERS:
    return f'\033[{CURSOR_CODES[action]}'
  msg = f"Invalid cursor action: '{action}'"
  raise ValueError(msg)


def clear(action: ClearActionNameType = 'all') -> str:
  """
  Get the ANSI escape code for the specified clear action.

  Parameters
  ----------
  action : ClearActionNameType,, default 'all'
      The clear action to perform.

  Returns
  -------
  str :
      The ANSI escape code for the specified clear action.

  Examples
  --------
  >>> clear()
  >>> clear('all')
  >>> clear('line')
  """
  return f'\033[{CLEAR_CODES[action]}'
