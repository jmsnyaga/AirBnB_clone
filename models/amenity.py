#!/usr/bin/python3
"""
Defines the Amenity class, which represents amenities available in a property.
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents an Amenity in the system, such as a pool or Wi-Fi."""

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.
        Inherits unique ID, creation, and update timestamps from BaseModel.
        """
        super().__init__(*args, **kwargs)
