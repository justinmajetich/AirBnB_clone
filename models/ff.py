

r = "State name=\"Addis_Ababa\" id=2"

ref = r.split()
cls = ref.pop(0)


new = {}

for i in ref:
    r = i.split('=')
    #cls.r[0] = r[1]
    new[r[0]] = r[1]

print(new['name'])
print(eval(new['name']))

print(eval("66"))

def split_args( args):
    new = args.split()
    return new
com = "Place name='AddisAbaba'"
new = split_args(com)
classname= new.pop(0)
print(new)
print()

name= '"abrahm"'
print(name.strip("'"))

try:
    if args:
        new_args = split_args(args)
        class_name = new_args.pop(0)
        new_dict = tokenize(new_args)
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        for k, v in new_dict.items():
            try:
                if type(eval(v)) is str:
                    v = v.replace("_", " ")
                exec(f'new_instance.{k} = {v}')
                print(new_instance.name)
            except Exception:
                continue
        storage.save()
        print(new_instance.id)
        storage.save()
except IndexError:
    print("** class name missing **")
    return
