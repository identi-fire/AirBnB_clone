#!/usr/bin/python3

"""
BaseModel class
"""


import uuid
from datetime import datetime, date, time


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        initializes the class
        """
        if len(kwargs) != 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.name = type(self).__name__

            # modify kwargs
            kwargs.pop('__class__')
            update = kwargs['updated_at']
            created = kwargs['created_at']
            kwargs['updated_at'] = datetime.strptime(
                update, '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(
                created, '%Y-%m-%dT%H:%M:%S.%f')

            # update current __dict__ with kwargs
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """
        returns the class data in readable format
        """
        data = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return data

    def save(self):
        """
        updates instance attribute saved at with the current datetime
        """
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """
        returns a dictionary containing instance data
        """
        self.save()
        modified = {}
        modified.update(data)
        modified['__class__'] = type(self).__name__
        modified['updated_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        modified['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')

        return modified
