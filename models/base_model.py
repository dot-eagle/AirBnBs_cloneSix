#!/usr/bin/python3
"""BaseModel Module:
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
import models
from uuid import uuid4


fomat = "%Y-%m-%dT%H:%M:%S.%f"
datenow = datetime.now()

class BaseModel:
    """ Base model class def """
    def __init__(self, *args, **kwargs):
        """ init constructor """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], fomat)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], fomat)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datenow
            self.updated_at = datenow
            models.storage.new(self)

    def save (self):
        """ save and updates method """
        self.updated_at = datenow
        models.storage.save()

    def __str__(self):
        """String representation method """
        return "[{}] ({}) {}".format(type(self).__name__,
                self.id, self.to_dict())

    def to_dict(self):
        """ Convert to dictionary format"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return (new_dict)

    def to_json(self):
        """ convert to json format """
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if isinstance(value, (datetime, uuid.UUID, tuple, set)):
                if type(value) is datetime:
                    value = value.isoformat()
                new_dict.update({key: str(value)})
        new_dict['__class__'] = str(self.__class__.__name__)
        return (new_dict)

