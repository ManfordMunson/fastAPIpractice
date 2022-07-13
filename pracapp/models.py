from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Dog(Base):
    """Creates the Dog Table."""

    __tablename__ = "dogs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey("owner.id"))


class Owner(Base):
    """Creates the Owner Table."""

    __tablename__ = "owner"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    paid = Column(Boolean)
    dogs = relationship("Dog")


class Payments(Base):
    """Creates the Payments Table."""

    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Float)
