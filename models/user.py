#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user in the system with basic attributes."""

    # User-specific attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        Calls the parent class's initialization to handle unique ID,
        creation and update timestamps.
        """
        super().__init__(*args, **kwargs)
