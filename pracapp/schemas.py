from pydantic import BaseModel

from .database import Base


class DogBase(BaseModel):
    """Is the Base Model for the Dog Class."""

    name: str
    age: int
    breed: str


class Dog(DogBase):
    """Initializes the Dog Class."""

    id: int
    owner_id: int

    class Config:
        """Configuress orm_mode for Dog Class"""

        orm_mode = True


class OwnerBase(BaseModel):
    """Is the Base Model for the Owner Class."""

    name: str
    paid: bool


class Owner(OwnerBase):
    """Initializes the Owner Class."""

    id: int
    dogs = list[Dog]

    class Config:
        """Configures orm_mode for Owner Class"""

        orm_mode = True


class PayBase(BaseModel):
    """Is the Base Model for the Pay Class."""

    name: str
    amount: float


class Pay(PayBase):
    """Initializes the Pay Class."""

    id: int

    class Config:
        """Configures orm_mode for Pay Class"""

        orm_mode = True
