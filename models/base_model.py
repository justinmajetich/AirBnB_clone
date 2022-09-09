#!/usr/bin/python3
"""
contains BaseModel definitions.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initializes object using dictionary if given otherwise
        it gives default value
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs['created_at']:
                # print("not new instance updating time === ")
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            else:
                # print("=====new instance  new time === ")
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        if len(args) >= 1:
            # print("========= args  ============= ")
            # print(args[0])
            # print(len(args[0]))
            self.create(args[0], self)

    def __str__(self):
        """string repr of obj"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def uwu(self, instance):
        print("let's go boys")
        print(instance)

    def update(self, args, instance):
        """update an obect instance by ID"""
        marker = 0
        if len(args) >= 3:
            attrs = args[2:]
            for idx in range(len(attrs)):
                # print("========== attr len , marker ==========")
                # print(len(attrs), marker + 1)
                if marker + 1 >= len(attrs):
                    break
                trimed = attrs[marker:marker + 2]
                # print(f"------------- attrs in loop # {idx}")
                self.add_attributes(instance, trimed, args[0])
                self.updated_at = datetime.now()
                marker += 2
        else:
            print("insuficient arguments")

    def create(self, args, instance):
        """helper function to create a class instance with args """
        # print("self in create === ", self)
        # for idx in range(len(args)):
        #     if idx % 2 == 0:
        #         for k, v in storage.attributes().items():
        #             if 1:
        marker = 0
        if len(args) >= 3:

            attrs = args[1:]

            for idx in range(len(attrs)):
                # print("========== attr len , marker ==========")
                # print(len(attrs), marker + 1)
                if marker + 1 >= len(attrs):
                    break
                trimed = attrs[marker:marker + 2]
                # print(f"------------- attrs in loop # {idx}")
                self.add_attributes(instance, trimed, args[0])
                marker += 2

    def add_attributes(self, instance, attr_list, c_name):
        """ function to insert attribute values,
        recieves a list index 0 is the attribute name
        and index 1 is the atrribute vallue """
        # print("-----  atr list --------")
        # print(attr_list)
        
        if len(attr_list) == 1:
            print(f"value for attribute {attr_list[0]} is missing")
        try:
            if self.attributes()[c_name][attr_list[0]]:
                # print(f"{c_name} ## {attr_list[0]}:{attr_list[1]}")
                setattr(instance, attr_list[0], attr_list[1])
                # print(attr_list)

        except KeyError:
            print(f"attribute {attr_list[0]} doesn't exist in class {c_name}")
            setattr(instance, attr_list[0], attr_list[1])

    def to_dict(self):
        """returns a dictionary containing all key/value of __dict__
        of the instance"""
        dic = vars(self).copy()
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        return dic

    def strip_quotes(self, str):
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

    def attributes(self):
        """Returns the valid attributes and their types for classname."""

        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.now(),
                 "updated_at": datetime.now()},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},

            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": str},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
