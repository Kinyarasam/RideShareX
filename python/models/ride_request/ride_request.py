#!/usr/bin/env python3
"""
Contains class RideRequest
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime


class RideRequest(BaseModel, Base):
    """
    Representation of a ride request
    """
    __tablename__ = "ride_requests"

    ride_id = Column(String(60), ForeignKey("rides.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    origin = Column(String(60), nullable=False)
    destination = Column(String(60), nullable=False)
    departure_at = Column(DateTime)
    arrive_at = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """
        Initializes ride request
        """
        super().__init__(*args, **kwargs)
