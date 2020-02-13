#!/usr/bin/python3
""" Console Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    prompt = '(hbnb)'

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
