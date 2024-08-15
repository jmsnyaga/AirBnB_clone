#!/usr/bin/python3
"""
Custom module containing the Review class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Customized class representing a Review."""

    place_id = ""
    user_id = ""
    text = ""
