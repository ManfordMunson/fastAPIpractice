from sqlalchemy import BOOLEAN, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Dog(Base):
    __tablename__ = "dogs"
    id = Column(Integer, primary_key = True, index =True)
    name = Column(String)
    owner = Column(String)
    breed = Column(String)
    age = Column(Integer)

    #owners = relationship("Owner", back_populates="dogs")


class Owner(Base):
    __tablename__ = "owner"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    paid = Column(BOOLEAN)
    
    #dogs = relationship("Dog", back_populates="owner")
