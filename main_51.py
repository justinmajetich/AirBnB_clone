#!/usr/bin/python3
""" Test
"""
import os

if os.path.exists("file.json"):
    os.remove("file.json")

from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City


if os.path.exists(FileStorage._FileStorage__file_path):
    os.remove(FileStorage._FileStorage__file_path)


fs = FileStorage()

# All with nothing
all_objs = fs.all()
if len(all_objs.keys()) > 0:
    print("all() is returning result when it should not")
    exit(1)

# Create 2 States and 1 city
search_keys = []
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
search_keys.append("{}.{}".format("State", new_state.id))

new_state = State()
new_state.name = "Nevada"
fs.new(new_state)
fs.save()
search_keys.append("{}.{}".format("State", new_state.id))

new_city = City()
new_city.name = "Las Vegas"
new_city.state_id = new_state.id
fs.new(new_city)
fs.save()
city_search = "{}.{}".format("City", new_city.id)

all_objs = fs.all(State)
if len(all_objs.keys()) != 2:
    print("all() is not returning all new State/City created")
    exit(1)

for key_search in search_keys:
    if all_objs.get(key_search) is None:
        print("State created should be in the list of objects")
        exit(1)
        
if all_objs.get(city_search) is not None:
    print("City created should not be in the list of objects if filtered by State")
    exit(1)
    
print("OK", end="")