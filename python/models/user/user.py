#!/usr/bin/env python3
"""
Contains class User
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5


class User(BaseModel, Base):
    """
    Representation of a user
    """
    __tablename__ = "user"

    email = Column(String(128), nullable=False)
    password = Column(String(128))
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes user
        """
        super().__init__(*args, **kwargs)

    def __setattr__(self, __name, __value):
        """
        Sets a password with md5 encryption
        """
        if __name == "password":
            __value = md5(__value.encode()).hexdigest()
        return super().__setattr__(__name, __value)
