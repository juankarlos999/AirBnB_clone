#!/usr/bin env python3
"""Define attributes
"""

from datetime import datetime
import uuid
from models.base_model import BaseModel
import models


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        value = obj.to_dict()
        my_new_obj = FileStorage.__objects.setdefault(key, obj)

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            file.write(my_json)

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
