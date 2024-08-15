#!/usr/bin/python3
"""
Defines the Place class, representing accommodations in the application.
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a Place available for rent."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Place instance.
        Inherits unique ID, creation, and update timestamps from BaseModel.
        """
        super().__init__(*args, **kwargs)
