#!/usr/bin/python3
"""Console for HBnB project."""
import cmd
import json
from shlex import split
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import base_model, user, place, state, city, amenity, review
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sys

storage = FileStorage()
storage.reload()

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        if '(' not in line or ')' not in line:
            return line

        cmd_class = line.split('(')
        if len(cmd_class) != 2:
            return line

        command = cmd_class[0]
        args = cmd_class[1].replace(')', '')

        if '.' not in command:
            return line

        try:
            class_name, command = command.split('.')
            if class_name not in HBNBCommand.classes:
                return line

            if command not in HBNBCommand.dot_cmds:
                return line

            if args.startswith('{') and args.endswith('}'):
                try:
                    args_dict = json.loads(args)
                except ValueError:
                    return line
            else:
                args_list = shlex.split(args)
                args_dict = dict(item.split('=') for item in args_list)

            obj = storage.all().get(class_name + '.' + args_dict.get('id'))
            if obj is None:
                return line

            setattr(obj, 'created_at', datetime.strptime(
                obj.created_at, '%Y-%m-%dT%H:%M:%S.%f'))
            setattr(obj, 'updated_at', datetime.strptime(
                obj.updated_at, '%Y-%m-%dT%H:%M:%S.%f'))

            if command == 'update':
                setattr(obj, **args_dict)
                obj.save()

            elif command == 'show':
                print(obj)

            elif command == 'destroy':
                storage.delete(obj.id)
                storage.save()

            elif command == 'all':
                obj_list = []
                for key, value in storage.all().items():
                    if class_name in key:
                        obj_list.append(value.__str__())
                print(obj_list)

            elif command == 'count':
                count = 0
                for key in storage.all():
                    if class_name in key:
                        count += 1
                print(count)

        except Exception:
            return line

    def postcmd(self, stop, line):
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def emptyline(self):
        pass
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, args):
        try:
            if not args:
                raise SyntaxError("** class name missing **")
            my_args = args.split(" ")

            kwargs = {}
            for i in range(1, len(my_args)):
                key, value = tuple(my_args[i].split("="))
                if value == '=':
                    value = value.strip('=').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
            if kwargs == {}:
                obj = eval(my_args[0])()
            else:
                obj = eval(my_args[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def help_create(self):
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        print_list = []

        objects = storage.all()
        print_list = []
        if not args:
            for key in objects:
                print_list.append(objects[key])
            print(print_list)
            return
        try:
            args = args.split(" ")
            if args[0] not in self.classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    print_list.append(objects[key])
            print(print_list)
        except NameError:
            print("** class doesn't exist **")

    def help_all(self):
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        count = 0
        for k, v in storage.all().items():
            if args in k:
                count += 1
        print(count)

    def help_count(self):
        print("Counts the number of instances for a class")

    def do_update(self, args):
        c_name = c_id = att_name = att_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found **")
            return

        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            if not att_name and args[0] != ' ':
                att_name = args[0]
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):
            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)
                new_dict.__dict__.update({att_name: att_val})
                new_dict.save()

    def help_update(self):
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")
        
    def do_EOF(self, line):
        """Handle the EOF (Ctrl+D) command to exit the CLI."""
        print()  # Print a newline for a cleaner exit
        return True  # Return True to exit the CLI

if __name__ == "__main__":
    HBNBCommand().cmdloop()
