#!/usr/bin/env python3
"""
Contains class Ride
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer, Boolean
from sqlalchemy.orm import relationship


class Ride(BaseModel, Base):
    """
    Representation of a ride
    """
    __tablename__ = "rides"

    plate_no = Column(String(60), nullable=False, unique=True)
    capacity = Column(Integer)
    isActive = Column(Boolean, nullable=False, default=False)
    ride_requests = relationship('RideRequest',
                                backref="ride",
                                cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """
        Initializes ride
        """
        super().__init__(*args, **kwargs)
