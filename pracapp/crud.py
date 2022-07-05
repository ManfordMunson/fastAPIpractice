from pyexpat import model
from unicodedata import name
from unittest import skip
from sqlalchemy.orm import Session

from . import models, schemas

def get_dog(db: Session):
    return db.query(models.Dog).all()

def create_dog(db: Session, dog: schemas.DogCreate):
    db_dog = models.Dog(name=dog.name, owner=dog.owner, age=dog.age, breed=dog.breed)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def get_owner(db: Session,name:str):
    return db.query(models.Dog).all()

def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(name=owner.name, paid=owner.paid)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner