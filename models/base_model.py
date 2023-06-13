#!/usr/bin/python3
"""
The class ``BaseModel`` defines all common attributes/methods for other classes
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """
    Define the class ``BaseModel``
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a ``BaseModel`` instance

        NB:
            args = not used
            kwargs = for creating an instance from a dictionary
            ``created_at`` and ``updated_at`` found in kwargs is a string
            format of time in ``isoformat``.
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            # created_at and updated_at should be the same for new instances
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Return the non-canonical string representation of
        ``BaseModel`` instance
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute ``updated_at``
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
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
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
