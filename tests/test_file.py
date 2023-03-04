#!/usr/bin/env python3
"""
Test the console.py interpreter with object creation using parameters.
"""

from console import HBNBCommand
from io import StringIO
import sys

if __name__ == '__main__':
    # Redirect stdout to a buffer for testing output
    stdout = sys.stdout
    sys.stdout = StringIO()

    # Test object creation with parameters
    cmd = HBNBCommand()
    cmd.onecmd('create State name="California"')
    cmd.onecmd('create State name="Arizona"')
    cmd.onecmd('all State')
    cmd.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
    cmd.onecmd('all Place')

    # Get the output from the buffer and reset stdout
    output = sys.stdout.getvalue()
    sys.stdout = stdout

    # Check that the output is correct
    expected_output = "California\nArizona\n[State.1, State.2]\nPlace.1\n[Place.1]\n"
    assert output == expected_output, f"Output does not match expected:\n{output}"
