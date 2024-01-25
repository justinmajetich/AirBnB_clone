#!/usr/bin/python3
from tmp_console import *
import tmp_console
from models import *

class ###FAKE_CLASS_NAME###(tmp_console.###FAKE_CLASS_NAME###):
    
    def do_create(self, args):
        """FAKE create
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        else:
            if len(args) > 0 and args[0] in HBNBCommand.valid_classes:
                params = {}
                if len(args) > 1:
                    for a in args[1:]:
                        s_a = a.split("=")
                        if '"' in s_a[1]:
                            params[s_a[0]] = s_a[1][1:-1].replace("_", " ")
                        # No integer and float management
                new_obj = eval(args[0])(**params)
                print(new_obj.id)
                new_obj.save()
            else:
                return
        

if __name__ == '__main__':
    ###FAKE_CLASS_NAME###().cmdloop()
