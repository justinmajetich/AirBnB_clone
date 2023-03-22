#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
print("All States: {}".format(fs.all(State)))

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
print("All States: {}".format(fs.all(State)))

# Delete the new State
fs.delete(new_state)

# All States
print("All States: {}".format(fs.all(State)))

