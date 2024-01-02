import os
import re
from datetime import datetime as dt
from lib.programClass import Program, Schedule

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
