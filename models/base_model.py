#!/usr/bin/python3
"""
This module defines the BaseModel class, serving as the foundation for other classes in the project.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class that defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        - If kwargs are provided, they are used to set attributes (for deserialization).
        - Otherwise, a new instance is created with a unique ID and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in {'created_at', 'updated_at'}:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance into a dictionary format.
        - The dictionary includes all instance attributes.
        - Dates are converted to ISO format strings.
        - The class name is also included.
        """
        result_dict = self.__dict__.copy()
        result_dict.update({
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
        })
        return result_dict
