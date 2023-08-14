#!/usr/bin/python3
"""
This module is the base class

"""
import uuid
from datetime import datetime
import models
#from models import storage


class BaseModel:
    """
    this is the class Basemodel that all other class in
    the project would inherite from

    """
    def __init__(self, *args, **kwargs):
        """
        this method initializes a new instance of the BaseModel
        it assigns a unique ID and sets time for creation and updating of time

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        try:
                            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        except ValueError as e:
                            print("Datetime parsing error:", e)
                            print("Datetime string:", value)
                            print("Expected format:", '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
        this method returns a string representation of the BaseModel instance
        with this format [<class name>] (<self.id>) <self.__dict__>

        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        This method update the public instance attribute updated_at with
        the current datetime

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        this method converts the instance attributes to a dictionary

        Returns:
            dict: A dictionary containing all keys/values of __dict__.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
