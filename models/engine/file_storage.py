#!/usr/bin/python3
"""
File storage class
"""


import json


class FileStorage:
    """
    file storage class serializes instance to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
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
        if obj is not None:
            # check content of obj
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize __objects to JSON file path
        """
        # modify __objects
        json_objects = {}
        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as f:
            for key, value in FileStorage.__objects.items():
                json_objects[key] = value.to_dict()
            json.dump(json_objects, f)

    def reload(self):
        """
        deserialize the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_data = json.load(f)

                for value in json_data.values():
                    className = value["__class__"]
                    self.new(eval(className)(**value))
            FileStorage.__objects = json_data
        except (NameError, FileNotFoundError):
            pass
