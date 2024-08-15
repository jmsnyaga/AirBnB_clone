#!/usr/bin/python3
"""This module initializes the 'models' package, setting up the storage system."""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage to manage object storage.
storage = FileStorage()

# Load any objects previously saved in the storage file into memory.
storage.reload()
