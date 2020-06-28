#!/usr/bin/python3
"""Create unique FileStorage instance"""

from models.engine.file_storage import FileStorage
from models import BaseModel


storage = FileStorage()
storage.reload()
