#!/usr/bin/python3
"""
Module that convert the dictionary representation to a JSON string
"""
import json


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Method that returns the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)

        Variables:

        * Attribute: __objects = {} from class FileStorage
        content:
        * Key = (name class) object BaseModel + attribute (id) from class
        (id, updated_at, created_at, __class__ and *args, **kwargs(optional))

        * Values = dictionary that content:
        (id, updated_at, created_at, __class__ and *args, **kwargs(optional))
        attributes from class BaseModel
        """
        new_obj = {}
        for key, value in FileStorage.__objects.items():
            new_obj[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file_save:
            json.dump(new_obj, file_save)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)exists
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as load_file:
                from models.amenity import Amenity
                from models.base_model import BaseModel
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User
                obj_load = json.load(load_file)
                for key, value in obj_load.items():
                    obj = eval(value["__class__"] + "(**value)")
                    FileStorage.__objects[key] = obj
        except:
            pass
