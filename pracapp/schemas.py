from datetime import datetime
from sqlite3 import Date
from pydantic import BaseModel
from sqlalchemy import Integer

from .database import Base

class DogBase(BaseModel):
    name: str
    owner: str
    age: int
    breed: str

class DogCreate(DogBase):
    pass

class Dog(DogBase):
    id: int
    
    class Config:
        orm_mode =True 

class OwnerBase(BaseModel):
    name: str
    paid: bool
    
class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True

class PayBase(BaseModel):
    name: str
    amount: float

class PayCreate(PayBase):
    pass

class Pay(PayBase):
    id: int
    
    class Config:
        orm_mode = True

