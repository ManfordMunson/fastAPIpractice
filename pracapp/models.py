from xmlrpc.client import DateTime
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

#Creates the Dog table
class Dog(Base):
    __tablename__ = "dogs"
    id = Column(Integer, primary_key = True, index =True)
    name = Column(String)
    owner = Column(String)
    breed = Column(String)
    age = Column(Integer)

    #owners = relationship("Owner", back_populates="dogs")

#Creates the Owner table 
class Owner(Base):
    __tablename__ = "owner"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    paid = Column(Boolean)
    
    #dogs = relationship("Dog", back_populates="owner")

class Payments(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    amount = Column(Float)