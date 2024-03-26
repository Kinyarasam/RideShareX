#!/usr/bin/env python3
"""
Initializes the models package
"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
