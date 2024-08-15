#!/usr/bin/python3
"""
Defines the City class, representing cities in the application.
"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a City within a state."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.
        Inherits unique ID, creation, and update timestamps from BaseModel.
        """
        super().__init__(*args, **kwargs)
