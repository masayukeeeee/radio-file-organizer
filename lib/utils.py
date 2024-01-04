"""
This file is for utility functions.

Methods:
    - is_unnamed_file: check if the file is unnamed file.
"""

import re


def is_unnamed_file(fn: str):
    """
    Check if the file is unnamed file.
    Args:
        fn (str): file name
    Returns:
        bool: True if the file is unnamed file
    """
    prog = re.compile(r'^AM\d{6}-\d{4}.MP3$')
    result = prog.match(fn)
    return result
