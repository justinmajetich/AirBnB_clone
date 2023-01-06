#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.user import User
fs = FileStorage()
# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
 print(all_states[state_key])
# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))
# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
 print(all_states[state_key])
# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))
# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
 print(all_states[state_key]) 
# test fs.all()
all_users = fs.all(User)
print("All Objects: {}".format(len(fs.all().keys())))
print("All States: {}".format(len(all_states.keys())))
print("All Users: {}".format(len(all_users.keys())))
# Delete the new State
fs.delete(new_state)
# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
 print(all_states[state_key])
# Delete the another State
fs.delete(another_state)
# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
all_users = fs.all(User)
print("All Users: {}".format(len(all_users.keys())))
