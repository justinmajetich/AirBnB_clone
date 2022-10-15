#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# my_model = BaseModel()
# my_model = User()
# my_model = Place()
# my_model = State()
# my_model = City()
# my_model = Amenity()
my_model = Review()

my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)

print('<---->')
my_model.save()
print(storage._FileStorage__objects.get(
    f"{my_model.__class__.__name__}.{my_model.id}"))
print(my_model)

print('<---->')
my_model_json = my_model.to_dict()
print(my_model_json)

print('<---->')
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
                                   type(my_model_json[key]),
                                   my_model_json[key]))

print('<---->')
my_model.delete()
print(storage._FileStorage__objects.get(
    f"{my_model.__class__.__name__}.{my_model.id}"))
