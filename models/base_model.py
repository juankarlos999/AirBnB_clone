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
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.id = str(uuid4())

    def save(self):
        """
        updates the public instance updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now().isoformat()
        return self.updated_at

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
