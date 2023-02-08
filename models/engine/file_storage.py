#!/usr/bin/python3

"""
File storage class
"""


import json


class FileStorage:
    """
    file storage class serializes instance to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = ""
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = type(obj).__name__.id
        self.__objects[key] = obj

    def save(self):
        """
        serialize __objects to JSON file path
        """
        with open(self.__file_path, "w") as file:
            json.dumps(self.__objects, file, indent=4)

    def reload(self):
        """
        deserialize the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                self.__objects.update(data)
        except FileNotFoundError:
            pass
