#!/usr/bin/python3
"""BaseModel class for AirBnB clone"""
import uuid
from datetime import datetime, date, time
from models import storage


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
            dt_f = '%Y-%m-%dT%H:%M:%S.%f'
            updated = datetime.strptime(kwargs['updated_at'], dt_f)
            created = datetime.strptime(kwargs['created_at'], dt_f)
            kwargs['updated_at'] = updated
            kwargs['created_at'] = created

            # update current __dict__ with kwargs
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing instance data
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
