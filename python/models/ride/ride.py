#!/usr/bin/env python3
"""
Contains class Ride
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Ride(BaseModel, Base):
    """
    Representation of a ride
    """
    __tablename__ = "ride"

    plate_no = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes ride
        """
        super().__init__(*args, **kwargs)
