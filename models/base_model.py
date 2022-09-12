#!/usr/bin/python3
"""
contains BaseModel definitions.
"""
import uuid
from datetime import datetime
from rich import print as rprint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()

Base = declarative_base()


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    """initializes obect for the db storage"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

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
                self.created_at = datetime.strptime(kwargs["created_at"], time)
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                # print("=====new instance  new time === ")
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # models.storage.new(self)
        if len(args) >= 1:

            self.create(args[0], self)

    def __str__(self):
        """string repr of obj"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def update(self, args, instance):
        """update an obect instance by ID"""
        marker = 0
        if len(args) >= 3:
            attrs = args[2:]
            for idx in range(len(attrs)):
                if marker + 1 >= len(attrs):
                    break
                trimed = attrs[marker:marker + 2]
                self.add_attributes(instance, trimed, args[0])
                self.updated_at = datetime.now()
                marker += 2
        else:
            print("insuficient arguments")

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def create(self, args, instance):
        """helper function to create a class instance with args """
        marker = 0
        if len(args) >= 3:
            attrs = args[1:]
            for idx in range(len(attrs)):
                if marker + 1 >= len(attrs):
                    break
                trimed = attrs[marker:marker + 2]
                self.add_attributes(instance, trimed, args[0])
                marker += 2

    def add_attributes(self, instance, attr_list, c_name):
        """ function to insert attribute values,
        recieves a list index 0 is the attribute name
        and index 1 is the atrribute vallue """
        if len(attr_list) == 1:
            print(f"value for attribute {attr_list[0]} is missing")
        try:
            if self.attributes()[c_name][attr_list[0]]:
                attr_val = attr_list[1]
                if '_' in attr_val and type(attr_val) == str:
                    attr_val = attr_val.replace('_', " ")
                setattr(instance, attr_list[0], attr_val)
        except KeyError:
            rprint(
                f"attr [bold spring_green2]{attr_list[0]}[/bold spring_green2]"
                f" doesn't exist in class [bold yellow]{c_name}[bold yellow] ")

    def to_dict(self):
        """returns a dictionary containing all key/value of __dict__
        of the instance"""
        dic = vars(self).copy()
        dic['__class__'] = self.__class__.__name__
        if "updated_at" in dic:
            dic['updated_at'] = self.updated_at.isoformat()
        if "created_at" in dic:
            dic['created_at'] = self.created_at.isoformat()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

    def strip_quotes(self, str):
        """"helper functoin to parse a string and remove quotes"""
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
