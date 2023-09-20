#!/usr/bin/python3
"""State Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class
    Att:
        name: entry name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
