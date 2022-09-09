#!/usr/bin/python3
""" Console Module """
import cmd
from curses.ascii import isupper
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import datetime
import re


from rich import print as rprint


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
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
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def parseline(self, line):
        """ cmd function that we'll override to intercept incomming commands
        and return standardly parsed commands for easr of use
        """

        """my custom quit function"""
        # case 1
        if line == '.':
            return cmd.Cmd.parseline(self, "quit")
        # case 2
        if '.' in line and '(' not in line and ')' not in line:
            """condition checks for commands like <User.create> or 
            <create.User> and converts them to create User"""
            toks = line.split('.')
            # self.printme("toks", toks)
            line = self.parseLineWithNoArgs(toks, line)
        # case 3
        if '.' not in line and '(' in line and ')' in line:
            """condition checks for commands like <User create(args...)> or
            <create User(args...)> and converts them to create User args..."""
            toks = line.replace('(', ' ').replace(')', ' ').replace(
                '=', ' ').replace('"', ' ')
            toks = toks.split(' ')
            payload = self.list_to_string(toks[2:])
            # self.printme("toks PAYLOAD", payload)
            newline = toks[1] + ' ' + toks[0] + ' ' + payload
            # self.printme("toks NEW LINE", newline)
            if len(toks) > 1 and toks[0][0].isupper():
                line = toks[1] + " " + toks[0] + " " + payload
            elif len(toks) > 1 and toks[1][0].isupper():
                line = toks[0] + " " + toks[1] + " " + payload
            # line = self.parseLineWithNoArgs(toks, line)
            # self.printme("toks FINAL LINE", line)

        # case 4
        if '.' in line and '(' in line and ')' in line:
            """ intercepts commands with .() notation and extracts the
            args into one strings"""
            toks = re.split(r'\.|\(|\)', line)
            # self.printme("args in if block", toks)

            payload = toks[2].strip('"').replace(',', ' ')
            # if payload[0] == '{' and payload[-1] == '}':
            # self.printme("messy payload ", payload)
            payload = self.dict_to_str(payload)
            # self.printme("sanitized payload ", payload)

            newline = toks[1] + ' ' + toks[0] + ' ' + payload
            if payload == '':
                if len(toks) > 1 and toks[0][0].isupper():
                    line = (toks[1], toks[0], newline)
                elif len(toks) > 1 and toks[1][0].isupper():
                    line = (toks[0], toks[1], newline)

            else:
                if len(toks) > 1 and toks[0][0].isupper():
                    line = (toks[1], toks[0] + " " + payload, newline)
                elif len(toks) > 1 and toks[1][0].isupper():
                    line = (toks[0], toks[1] + " " + payload, newline)

            if toks[1] == 'count':
                self.count(toks[0])
                return cmd.Cmd.parseline(self, '')

            return line
        # case 5
        else:
            """ intercepts regular all string commands to remove any quotes
            to output standadized text
            """
            args = line.split(" ")
            # self.printme("args in else block", args)
            # print("intercepted straight one")
            # pprint(args)
            payload = []

            # case 5A
            if len(args) > 2:
                """ for args the look like <create User args... > 
                or <User create args...> and converts 
                them to create User args,,,
                """
                self.printme("ARGS ", payload)
                payload = args[2:]
                # self.printme("raw payload ", payload)
                payload = self.list_to_string(payload)
                # self.printme("sanitized payload ", payload)
                # print("==== sanitized payload =====")
                # print(payload)
                newline = args[0] + ' ' + args[1] + ' ' + payload
                # line = (args[0], args[1] + " " + payload, newline)
                self.printme("args ", args)
                toks = args
                if len(toks) > 1 and toks[0][0].isupper():
                    line = (toks[1], toks[0] + " " + payload, newline)
                elif len(toks) > 1 and toks[1][0].isupper():
                    line = (toks[0], toks[1] + " " + payload, newline)
                # line = self.parseLineWithNoArgs(args, line, payload)
                # print("====== line =====")
                # self.printme("line in else block", line)
                return line
            # case 5B
            elif len(args) > 1:
                """ for args the look like <create User > or <User create> 
                and converts them to create User
                """
                toks = line.split(' ')
                line = self.parseLineWithNoArgs(toks, line)

        # self.printme("global line", line)
        return cmd.Cmd.parseline(self, line)

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        argslist = args.split(" ")
        # self.printme("inside do_create parsed ", parsed)
        c_name = argslist[0]

        if not c_name:
            print("** class name missing **")
            return
        elif c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[c_name](argslist)
        
        self.printme("new class instance created ", new_instance)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
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
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object. """

        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id == "all":
            for k, v in list(storage.all().items()):
                idclass = k.split('.')
                if idclass[0] == c_name:
                    self.delete_instance(idclass[0], idclass[1])

        else:
            self.delete_instance(c_name, c_id)

        storage.save()

    def delete_instance(self, name, id):
        """helper function for destroying an object instance"""
        if not name:
            print("** class name missing **")
            return

        if name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        key = name + "." + id
        try:
            del storage.all()[key]

        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)
        self.printme("all of instance ", print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] is '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    """ my custom helper functions for string maniputlation"""

    def dict_to_str(self, dict):
        """"converts  a dictionary like string to string for easier parsing"""
        dictlist = dict.split(' ')
        newstr = ""
        for idx in range(len(dictlist)):
            newword = ""
            for word in dictlist[idx]:
                if not word == '"' and not word == '' and not word == "'" and\
                    not word == "}" and not word == "{"   \
                        and not word == ":":
                    newword = "".join([newword, word])
            if len(newword) > 0:
                newstr += str(newword) + " "

        newstr = newstr.strip()
        if '=' in newstr:
            newstr = newstr.replace('=', ' ')
        # print("===== dict list =========")
        # print(newstr)
        return newstr

    def list_to_string(self, list):
        """ takes a list and spits out a string comprised of each
        list item separated by blank space  """
        newstr = ""
        for idx in range(len(list)):
            word = list[idx]
            newword = ""
            for chr in word:
                if not chr == '"' and not chr == '' and not chr == "'":
                    newword = "".join([newword, chr])

            # print("===== new word =========")
            # print(newword)
            if len(newword) > 0:
                newstr += str(newword) + " "

        newstr = newstr.strip()
        if '=' in newstr:
            newstr = newstr.replace('=', ' ')
        # print("===== list to str =========")
        # print(newstr)
        return newstr

    def strip_quotes(self, str):
        """removes quotes from strings for easier parsing"""
        if not str:
            return
        if str[0] == '"' and str[len(str) - 1] == '"':
            return str[1:len(str) - 1]
        elif str[0] == '"':
            return str[1:]
        elif str[len(str) - 1] == '"':
            return str[:len(str) - 1]
        else:
            return str

    def printme(self, title, body):
        """helper function to print items to console"""
        print(f" ====  {title} start =====")
        rprint(body)
        print(f" ====  {title} end =====")

    def parseLineWithNoArgs(self, toks, line, isTuple=False):
        """helper function to swap commands and Class to aciev 
         this structure create User """

        # self.printme("toks to parse ", toks)
        if len(toks) > 1 and toks[0][0].isupper():
            line = toks[1] + " " + toks[0]
        elif len(toks) > 1 and toks[1][0].isupper():
            line = toks[0] + " " + toks[1]
        # self.printme("line in args ", line)
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
