#!/usr/bin/python3
"""
this module is the filestorage class

"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import json


class FileStorage:
    """
    this class serializes and deserializes instances to and from JSON file

    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        this method returns the dictionary of objects

        """
        if cls is None:
            return self.__objects
        else:
            class_objs = {key: obj for key, obj in self.__objects.items() if cls == key.split('.')[0]}
            return class_objs

    def new(self, obj):
        """
        this method adds a new object to __objects

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
 
    def save(self):
        """
        serializes __objects to the JSON file

        """
        obj_dic = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dic, file, indent=4, default=self.json_serialize)
    
    def json_serialize(self, obj):
        """
        custom json serializer for handling datetime objects
        """
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def reload(self):
        """
        #this method deserializes the json file to __objects

        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']
                    obj = eval(class_name + '(**value)')
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass


    def count(self, cls=None):
        """
        Returns the number of instance of a class

        """
        if cls is None:
            return len(self.__objects)
        return len(self.all(cls))
    
