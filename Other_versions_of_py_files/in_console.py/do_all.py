# Task 2. Console improvements - all method alternative for obtaining
# same task output
def do_all(self, args):
    print_list = []

    if args:
        args = args.split(' ')[0]  # remove possible trailing args
        if args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for k, v in storage._FileStorage__objects.items():
            if k.split('.')[0] == args:
                print_list.append(v)
    else:
        for k, v in storage._FileStorage__objects.items():
            print_list.append(v)

    print(', '.join(map(str, print_list)))
