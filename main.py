#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import os

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")


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
state_id = exec_command(my_console, "create State name=\"California\"")
if state_id is None or state_id == "":
    print("FAIL: Can't create State")

city_id = exec_command(my_console, "create City state_id=\"{}\" name=\"Fremont\"".format(state_id))
if city_id is None or city_id == "":
    print("FAIL: Can't create City")

user_id = exec_command(my_console, "create User email=\"a@a.com\" password=\"pwd\" first_name=\"fn\" last_name=\"ln\"")
if user_id is None or user_id == "":
    print("FAIL: Can't create User")

place_id = exec_command(my_console, "create Place city_id=\"{}\" user_id=\"{}\" name=\"House\" number_rooms=4 number_bathrooms=2 max_guest=6 price_by_night=100 latitude=1.3 longitude=2.3".format(city_id, user_id))
if place_id is None or place_id == "":
    print("FAIL: Can't create Place")
    
print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
