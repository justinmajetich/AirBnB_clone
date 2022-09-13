

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
