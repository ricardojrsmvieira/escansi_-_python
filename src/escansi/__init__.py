"""
Escansi - A Python library for ANSI escape codes.

This package provides utilities for working with ANSI escape codes in Python.
"""

# ---> Local imports <--- #
from .types import (
    ClearActionNameType as ClearActionNameType,
    ColorNameType as ColorNameType,
    CursorActionNameType as CursorActionNameType,
    FormatNameType as FormatNameType,
)
from .utils import (
    back_color as back_color,
    clear as clear,
    cursor as cursor,
    fore_color as fore_color,
    format_text as format_text,
    reset_formats as reset_formats,
)
