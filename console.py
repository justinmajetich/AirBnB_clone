#!/usr/bin/python3
"""The Console"""

import re
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    - The command class defines the commands to
    be used in the user interactive mode.
    - Its the Frontend interface where the input commands are interpreted and
    sent to storage methods(backend logic)
    """
    prompt = "(hbnb) "

    class_list = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
        }

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        args_input = args.strip().split()
        if len(args_input) == 0:
            print("** class name missing **")
            return

        class_name = args_input[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        new_instance = self.class_list[class_name]()

        for param in args_input[1:]:
            if '=' not in param:
                continue

            key, value = param.split('=', 1)
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
                value = value.replace('\\"', '"')
                value = value.replace('_', ' ')

            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        args_input = args.strip().split()
        if len(args_input) == 0:
            print("** class name missing **")
            return

        class_name = args_input[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        elif len(args_input) < 2:
            print("** instance id missing **")
            return

        else:
            obj_id = args_input[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objs = storage.all()

            if key in all_objs.keys():
                print(all_objs[key])
            else:
                print("** no instance found **")
                return

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all
        """
        all_objs = storage.all()
        args_input = args.strip().split()

        if not args_input:
            print([str(obj) for obj in all_objs.values()])
            return

        else:
            class_name = args_input[0]

            if class_name not in self.class_list:
                print("** class doesn't exist **")
                return

            else:
                result = []
                for key, val in all_objs.items():
                    if key.startswith(class_name):
                        result.append(str(val))

                print(result)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args_input = args.strip().split()
        if len(args_input) == 0:
            print("** class name missing **")
            return

        class_name = args_input[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        if len(args_input) == 1:
            print("** instance id missing **")
            return

        obj_id = args_input[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args_input) == 2:
            print("** attribute name missing **")
            return

        attr_name = args_input[2]
        if attr_name in ("id", "created_at", "updated_at"):
            return

        if len(args_input) == 3:
            print("** value missing **")
            return

        attr_val = args_input[3]
        if attr_val.isdigit():
            attr_val = int(attr_val)
        else:
            try:
                attr_val = float(attr_val)
            except ValueError:
                attr_val = attr_val.strip('"').strip("'")

        obj = all_objs.get(key)
        setattr(obj, attr_name, attr_val)
        obj.save()

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        line_args = args.strip().split()
        class_name = line_args[0]
        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        elif len(line_args) == 1:
            print("** instance id missing **")
            return

        else:
            obj_id = line_args[1].strip('"')
            key = "{}.{}".format(class_name, obj_id)
            all_objs = storage.all()

            if key not in all_objs:
                print("** no instance found **")
                return
            else:
                storage.delete(all_objs[key])
                storage.save()

    def do_count(self, args):
        """Retrieve the number of instances of a class: <class name>.count()"""
        line_args = args.split()

        if not line_args:
            print("** class name missing **")

        else:
            class_name = line_args[0]

            if class_name in self.class_list:
                count = 0
                all_objs = storage.all()

                for key in all_objs.keys():
                    if key.startswith(class_name):
                        count += 1
                print(count)

            else:
                print("** class doesn't exist **")

    def default(self, args):
        """Handles operations of <class name>.<command>"""
        if '.' in args:
            class_name, method_call = args.split('.')

            if class_name not in self.class_list:
                print("** class doesn't exist **")
                return

            if method_call == "all()":
                self.do_all(class_name)

            if method_call == "count()":
                self.do_count(class_name)

            if method_call.startswith("show("):
                match = re.search(r'\(["\']?([^"\')]+)["\']?\)', method_call)
                if match:
                    obj_id = match.group(1)
                    self.do_show("{} {}".format(class_name, obj_id))

            if method_call.startswith("destroy("):
                match = re.search(r'\(["\']?([^"\')]+)[]"\']?\)', method_call)
                if match:
                    obj_id = match.group(1)
                    self.do_destroy("{} {}".format(class_name, obj_id))

            if method_call.startswith("update("):
                match = re.search(
                    r'update\(["\']?([^,"\']+)["\']?,'
                    r'\s*["\']?([^,"\']+)["\']?,\s*["\']?([^"\']+)["\']?\)',
                    method_call
                )
                if match:
                    obj_id, attr_name, attr_value = match.groups()
                    self.do_update(
                        "{} {} {} {}".format(
                                             class_name,
                                             obj_id,
                                             attr_name,
                                             attr_value)
                    )

                dict_match = re.search(r'update\(["\']([^,"\']+)["\']\s*,'
                                       r'\s*(\{.*\})\)', method_call)
                if dict_match:
                    obj_id = dict_match.group(1).strip()
                    attr_dict = eval(dict_match.group(2))
                    for attr_name, attr_value in attr_dict.items():
                        self.do_update(
                            "{} {} {} {}".format(
                                                 class_name,
                                                 obj_id,
                                                 attr_name,
                                                 attr_value)
                        )

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit program on ctrl + D"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
