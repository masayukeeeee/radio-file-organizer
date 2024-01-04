"""
Test for utils.py
"""
import re
from pathlib import Path
import pytest
from lib.utils import is_unnamed_file

ROOT_DIR = Path(__file__).resolve().parents[2]


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
