#!/usr/bin/python3
"""
The class ``BaseModel`` defines all common attributes/methods for other classes
"""

import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column,
        String,
        DateTime,
        ForeignKey
        )
from sqlalchemy.orm import (
        relationship
        )

"""
Note! BaseModel does /not/ inherit from Base. All other classes will \
inherit from BaseModel to get common values (id, created_at, updated_at), \
where inheriting from Base will actually cause SQLAlchemy to attempt to \
map it to a table.
"""
Base = declarative_base()


class BaseModel:
    """
    Define the class ``BaseModel``

    Class attributes:
    =================
    * id (String): represents a column containing a unique string (60 chars)
        * can't be null
        * primary key

    * created_at (DateTime): represents a column containing a datetime
        * can't be null
        * default value is the current datetime (use datetime.utcnow())

    * updated_at (DateTime): represents a column containing a datetime
        * can't be null
        * default value is the current datetime (use datetime.utcnow())
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """
        Initialize a ``BaseModel`` instance

        NB:
            args = not used
            kwargs = for creating an instance from a dictionary
            ``created_at`` and ``updated_at`` found in kwargs is a string
            format of time in ``isoformat``.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs is not None:
            for key, value in kwargs.items():
                # skip these keys
                if key in ["__class__", "_sa_instance_state_"]:
                    continue

                # for datetime objects
                if key in ["updated_at", "created_at"]:
                    fmt = "%Y-%m-%dT%H:%M:%S.%f"
                    kwargs[key] = datetime.strptime(kwargs[key], fmt)

                # Update instance with this key, value pair
                self.__dict__.update({key: value})

    def __str__(self):
        """
        Return the non-canonical string representation of
        ``BaseModel`` instance
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = dict()

        # Remove unnecesary attributes
        unnecessary_attr = ["_sa_instance_state"]
        for key, value in self.__dict__.items():
            if key in unnecessary_attr:
                continue
            else:
                dictionary.update({key: value})

        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """
        Update the public instance attribute ``updated_at``
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of ``__dict__``
        of the instance:
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})

        # Return a different format of datetime objects
        for key in ["created_at", "updated_at"]:
            if type(dictionary[key]) == datetime:
                dictionary[key] = self.created_at.isoformat()

        # Remove unnecessary key
        unnecessary_keys = ["_sa_instance_state"]
        final_dict = dict()
        for key, value in dictionary.items():
            if key in unnecessary_keys:
                # skip unnecessary attributes
                continue
            else:
                final_dict.update({key: value})

        return final_dict

    def delete(self):
        """
        Delete this instance from storage
        """
        models.storage.delete(self)
