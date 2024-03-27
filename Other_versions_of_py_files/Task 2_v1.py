# Task 2. Console improvements
def do_create(self, args):
    """Create an object of any class with given parameters."""
    arguments = args.split(' ')
    if not arguments or not arguments[0]:
        print("** class name missing **")
        return
    elif arguments[0] not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return

    # Create an instance of the specified class
    new_instance = HBNBCommand.classes[arguments[0]]()

    # Process each attribute=value pair
    for arg in arguments[1:]:
        if '=' not in arg:
            print(f"** attribute format error **: {arg} (expected key=value)")
            continue
        key, value = arg.split('=', 1)
        if not key or not value:
            print(f"** attribute format error **: {arg} (expected key=value)")
            continue
        # Assign the parsed value to the new instance
        setattr(new_instance, key, self.parse_value(value))

    # Save the new instance and print its id
    new_instance.save()
    print(new_instance.id)

# Task 2. Console improvements


def parse_value(self, value):
    """Parse a string value to the correct type."""
    if value[0] == '"' and value[-1] == '"':
        value = value.strip('"').replace('_', ' ').replace('\\"', '"')
        return value  # Return string value without converting to int/float
    elif '.' in value:
        try:
            return float(value)
        except ValueError:
            pass
    else:
        try:
            return int(value)
        except ValueError:
            pass
    return value  # Return the original value if it can't be converted
