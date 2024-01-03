# test for utils.py with pytest

import pytest
import os, sys
import re
from datetime import datetime as dt
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
SCR_DIR = ROOT_DIR / 'script'
TMP_DIR = ROOT_DIR / 'uncategorized'

sys.path.append(str(SCR_DIR))


from lib.utils import is_unnamed_file
from lib.programClass import Program, Schedule, RawItem

s = Schedule()
s.load_programs(SCR_DIR / 'program.json')

# parametrize
@pytest.mark.parametrize(
    'raw_name, expected',
    [
        ('AM240102-0101.mp3', None),
        ('AM240102-2211.Mp3', None),
        ('test', None)
    ]
)
def test_is_unnamed_file_error(raw_name, expected):
    """
    test for is_unnamed_file function.
    """
    actual = is_unnamed_file(raw_name)
    assert actual == expected

@pytest.mark.parametrize(
    'raw_name, expected',
    [
        ('AM240102-0101.MP3', re.Match)
    ]
)
def test_is_unnamed_file_ok(raw_name, expected):
    """
    [Normal type] test for is_unnamed_file function.
    """
    actual = is_unnamed_file(raw_name)
    assert actual.__class__ == expected