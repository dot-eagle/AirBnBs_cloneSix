#!/usr/bin/python3
"""FileStorage module."""

import os
import json
import Datetime
import uuid

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ add objects to instance """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def all(self):
        """ return dictionary __objects """
         return (FileStorage.__objects)

    def reload(self):
        """ Reload and serialize objects """
        try:
             with open(self.__file_path, 'r', encoding="UTF-8") as f:
                 for key, value in (json.load(f)).items():
                     value = eval(value["__class__"])(**value)
                     self.__objects[key] = value
        except Exception:
            pass

    def save(self):
        """ save objects """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
            
        """temp = {}
        for k, v in type(self).__objects.items():
            temp[k] = v.to_dict()
            with open(type(self).__file_path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(temp) + '\n') """

