#!/usr/bin/python3

import cmd
import models

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from console.unpack import UnpackingTool
from console.behaviour import *

console_members = UnpackingTool.activate(globals())

exit()
HBNBCommand = type(
    "HBNBCommand",
    (cmd.Cmd,),
    console_members
)
if __name__ == '__main__':
    HBNBCommand().cmdloop()