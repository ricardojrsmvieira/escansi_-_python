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
def ForeColor(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: None = None,
  blue: None = None,
  /
) -> str: ...
@overload
def ForeColor(
  color_or_grey_or_red: int,
  green: int,
  blue: int,
  /
) -> str: ...
#endregion overloads
def ForeColor(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: int | None = None,
  blue: int | None = None,
  /
) -> str:
  if isinstance(color_or_grey_or_red, str):
    if color_or_grey_or_red in COLOR_NAMES:
      return f"\033[{COLOR_CODES['foreground'][color_or_grey_or_red]}m"
    if color_or_grey_or_red.startswith('#') and len(color_or_grey_or_red) == 7:
      try:
        r = int(color_or_grey_or_red[1:3], 16)
        g = int(color_or_grey_or_red[3:5], 16)
        b = int(color_or_grey_or_red[5:7], 16)
        return f'\033[38;2;{r};{g};{b}m'
      except ValueError:
        raise ValueError(f"Invalid color code or name: '{color_or_grey_or_red}'")
    else:
      raise ValueError(f"Invalid color code or name: '{color_or_grey_or_red}'")
  elif green is None or blue is None:
    if isinstance(color_or_grey_or_red, tuple):
      r, g, b = color_or_grey_or_red
      return f'\033[38;2;{r};{g};{b}m'
    return f'\033[38;5;{color_or_grey_or_red}m'
  else:
    return f'\033[38;2;{color_or_grey_or_red};{green};{blue}m'


#region overloads
@overload
def BackColor(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: None = None,
  blue: None = None,
  /
) -> str: ...
@overload
def BackColor(
  color_or_grey_or_red: int,
  green: int,
  blue: int,
  /
) -> str: ...
#endregion overloads
def BackColor(
  color_or_grey_or_red: str | int | tuple[int, int, int],
  green: int | None = None,
  blue: int | None = None,
  /
) -> str:
  if isinstance(color_or_grey_or_red, str):
    if color_or_grey_or_red in COLOR_NAMES:
      return f"\033[{COLOR_CODES['background'][color_or_grey_or_red]}m"
    if color_or_grey_or_red.startswith('#') and len(color_or_grey_or_red) == 7:
      try:
        r = int(color_or_grey_or_red[1:3], 16)
        g = int(color_or_grey_or_red[3:5], 16)
        b = int(color_or_grey_or_red[5:7], 16)
        return f'\033[48;2;{r};{g};{b}m'
      except ValueError:
        raise ValueError(f"Invalid color code or name: '{color_or_grey_or_red}'")
    else:
      raise ValueError(f"Invalid color code or name: '{color_or_grey_or_red}'")
  elif green is None or blue is None:
    if isinstance(color_or_grey_or_red, tuple):
      r, g, b = color_or_grey_or_red
      return f'\033[48;2;{r};{g};{b}m'
    return f'\033[48;5;{color_or_grey_or_red}m'
  else:
    return f'\033[48;2;{color_or_grey_or_red};{green};{blue}m'


def Format(format: FormatNameType | tuple[FormatNameType, ...]) -> str:
  if isinstance(format, tuple):
    return ''.join(f"\033[{FORMAT_CODES['apply'][f]}m" for f in format)
  return f"\033[{FORMAT_CODES['apply'][format]}m"


def ResetFormat(format: FormatNameType | tuple[FormatNameType, ...] | Literal['all'] = 'all') -> str:
  if format == 'all':
    return '\033[0m'
  if isinstance(format, tuple):
    return ''.join(f"\033[{FORMAT_CODES['reset'][f]}m" for f in format)
  return f"\033[{FORMAT_CODES['reset'][format]}m"


#region overloads
@overload
def Cursor(
action: CursorActionsThatHaveNoNumberParametersNameType,
  n: None = None,
  m: None = None,
  /
) -> str: ...
@overload
def Cursor(
action: CursorActionsThatHaveOneNumberParameterNameType,
  n: int,
  m: None = None,
  /
) -> str: ...
@overload
def Cursor(
action: CursorActionsThatHaveTwoNumberParametersNameType,
  n: int,
  m: int,
  /
) -> str: ...
#endregion overloads
def Cursor(
  action: CursorActionNameType,
  n: int | None = None,
  m: int | None = None,
  /
) -> str:
  if action in CURSOR_ACTIONS_THAT_HAVE_ONE_NUMBER_PARAMETER:
    return f'\033[{n}{CURSOR_CODES[action]}'
  if action in CURSOR_ACTIONS_THAT_HAVE_TWO_NUMBER_PARAMETERS:
    return f'\033[{n};{m}{CURSOR_CODES[action]}'
  if action in CURSOR_ACTIONS_THAT_HAVE_NO_NUMBER_PARAMETERS:
    return f'\033[{CURSOR_CODES[action]}'
  raise ValueError(f"Invalid cursor action: '{action}'")


def Clear(action: ClearActionNameType = 'all') -> str:
  return f'\033[{CLEAR_CODES[action]}'
