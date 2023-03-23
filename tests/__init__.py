#!/usr/bin/python3
"""This file contains functions which can be used in all files within the tests
package
"""
from typing import TextIO
import sys
from io import StringIO


def reset_stream(stream: TextIO):
    """Resets the output stream"""
    if stream.seekable():
        stream.truncate(0)
        stream.seek(0)


def capture_output(callable):
    """Capture the standard output of a callable and return it as a string."""
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    callable()
    sys.stdout = old_stdout
    return captured_output.getvalue()
