#!/usr/bin/python3

"""
Module implementing the HBNBCommand class for the command-line interface.
"""

import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    """
    Class representing the command-line interface for the application.
    Inherits from the cmd.Cmd class.
    """
    prompt = '(hbnb) '
    storage.reload()

    valid_classes = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Method called when an empty line is entered.
        Does nothing to prevent default behavior.
        """
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True

    def do_create(self, args):
        """Create a new Basemodel"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) > 1:
            storage = self.parse_kwargs(args[1:])
            new_obj = eval(args[0])(**storage)
        else:
            new_obj = eval(args[0])()

        print(new_obj.id)
        new_obj.save()

    def do_show(self, args):
        """Usage: show BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        cls_objs = storage.all(args[0])
        for objs_id in cls_objs.keys():
            if objs_id == args[1] and args[0] in str(type(cls_objs[objs_id])):
                print(cls_objs[objs_id])
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """Usage: destroy BaseModel 1234-1234-1234"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        cls_objs = storage.all(args[0])
        for objs_id in cls_objs.keys():
            if objs_id == args[1]:
                storage.delete(cls_objs[objs_id])
                storage.save()
                return

        print("** no instance found **")

    def do_all(self, args):
        """Usage: all Basemodel or all"""
        if args not in HBNBCommand.valid_classes and len(args) != 0:
            print("** class doesn't exist **")
            return
        elif args in HBNBCommand.valid_classes:
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(args))}
        elif len(args) == 0:
            all_objs = storage.all()
        else:
            return
        for objs_id in all_objs.keys():
            print(all_objs[objs_id])

    def do_update(self, args):
        """Use: update <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        res = storage.update(args[0], args[1], args[2], args[3])
        if res == 0:
            print("** no instance found **")

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(<id>, <attribute name>, <attribute value>) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(<id>, <attribute name>, <attribute value>) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")

    @staticmethod
    def parse_kwargs(args):
        storage = {}
        for arg in args:
            pair = arg.split("=")
            if len(pair) == 2:
                if pair[1].startswith('"') and pair[1].endswith('"'):
                    pair[1] = pair[1][1:-1]
                    pair[1] = pair[1].replace("_", " ")
                elif "." in pair[1]:
                    try:
                        pair[1] = float(pair[1])
                    except:
                        continue
                else:
                    try:
                        pair[1] = int(pair[1])
                    except:
                        continue
                storage[pair[0]] = pair[1]
        return storage


if __name__ == '__main__':
    HBNBCommand().cmdloop()