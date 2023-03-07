#!/usr/bin/python3

import cmd
import models
from console.unpack import UnpackingTool
from console.behaviour import *

HBNBCommand = type(
    "HBNBCommand",
    (cmd.Cmd,),
    UnpackingTool.activate(globals())
)

if __name__ == '__main__':
    models.storage.reload()
    HBNBCommand().cmdloop()
