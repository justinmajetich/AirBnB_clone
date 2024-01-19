#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil

"""
Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)

"""
Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")

"""
Backup models/__init__.py file
"""
if os.path.exists("models/tmp__init__.py"):
    shutil.copy("models/tmp__init__.py", "models/__init__.py")
shutil.copy("models/__init__.py", "models/tmp__init__.py")

"""
Overwrite models/__init__.py file with switch_to_file_storage.py
"""
if os.path.exists("switch_to_file_storage.py"):
    shutil.copy("switch_to_file_storage.py", "models/__init__.py")

"""
Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

import console

"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Tests
"""
state_name = "California"
result = exec_command(my_console, "create State name=\"{}\"".format(state_name))
if result is None or result == "":
    print("FAIL: No ID retrieved")

state_id = result

city_name = "San Francisco is super cool"
result = exec_command(my_console, "create City state_id=\"{}\" name=\"{}\"".format(state_id, city_name.replace(" ", "_")))
# create City state_id="d363d0fc-509c-4b29-81d0-1ae0b4b7025f" city_name="San_Francisco_is_super_cool"
if result is None or result == "":
    print("FAIL: No ID retrieved")

city_id = result

user_email = "my@me.com"
user_pwd = "pwd"
user_fn = "FN"
user_ln = "LN"
result = exec_command(my_console, "create User email=\"{}\" password=\"{}\" frist_name=\"{}\" last_name=\"{}\"".format(user_email, user_pwd, user_fn, user_ln))
if result is None or result == "":
    print("FAIL: No ID retrieved")

user_id = result

place_name = "My house"
place_desc = "no description yet"
place_nb_rooms = 4
place_nb_bath = 0
place_max_guests = -3
place_price = 100
place_lat = -120.12
place_lon = 0.41921928
result = exec_command(my_console, "create Place city_id=\"{}\" user_id=\"{}\" name=\"{}\" description=\"{}\" number_rooms={} number_bathrooms={} max_guest={} price_by_night={} latitude={} longitude={}".format(city_id, user_id, place_name.replace(" ", "_"), place_desc.replace(" ", "_"), place_nb_rooms, place_nb_bath, place_max_guests, place_price, place_lat, place_lon))
if result is None or result == "":
    print("FAIL: No ID retrieved")

place_id = result

result = exec_command(my_console, "show Place {}".format(place_id))
if result is None or result == "":
    print("FAIL: empty output")

if "[Place]" not in result or place_id not in result:
    print("FAIL: wrong output format: \"{}\"".format(result))

if "city_id" not in result or city_id not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "user_id" not in result or user_id not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "name" not in result or place_name not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "description" not in result or place_desc not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "number_rooms" not in result or str(place_nb_rooms) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "number_bathrooms" not in result or str(place_nb_bath) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "max_guest" not in result or str(place_max_guests) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "price_by_night" not in result or str(place_price) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "latitude" not in result or str(place_lat) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))

if "longitude" not in result or str(place_lon) not in result:
    print("FAIL: missing new information: \"{}\"".format(result))


print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
