tmp_console import *
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
            print("fake")

if __name__ == '__main__':
    ###FAKE_CLASS_NAME###().cmdloop()
