#!/usr/bin/python3

""" Module of Base for AirBnB clone project
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Class BaseModel defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation method or constructor with *args and **kwargs
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid4())

    def save(self):
        """
        updates the public instance updated_at attribute
        with the current datetime
        """
        self.updated_at = datetime.now().isoformat()
        return self.updated_at

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        var_dict = self.__dict__.copy()
        var_dict["__class__"] = self.__class__.__name__
        var_dict["created_at"] = self.created_at.isoformat()
        var_dict["updated_at"] = self.updated_at.isoformat()
        return var_dict

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """
        print_ = "[{}] ({}) {}"
        return print_.format(self.__class__.__name__, self.id, self.__dict__)
