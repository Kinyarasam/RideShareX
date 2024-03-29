#!/usr/bin/env python3
"""
Contains class User
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """
    Representation of a user
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128))
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    ride_requests = relationship("RideRequest",
                                 backref="user")

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
    
    @classmethod
    def find(cls, *args, **kwargs):
        """
        Get a record matching the details provided
        """
        if "password" in kwargs.keys():
            kwargs["password"] = md5(kwargs["password"].encode()).hexdigest()

        return models.storage.find(cls, **kwargs)
