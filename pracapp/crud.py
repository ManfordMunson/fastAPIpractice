from importlib.util import module_for_loader
from pyexpat import model
from statistics import mode
from unicodedata import name
from unittest import skip
from sqlalchemy.orm import Session

from . import models, schemas

#Returns entire Dogs table
def get_dog(db: Session):
    return db.query(models.Dog).all()

#Adds a dog to the Dogs table 
def create_dog(db: Session, dog: schemas.DogCreate):
    db_dog = models.Dog(name=dog.name, owner=dog.owner, age=dog.age, breed=dog.breed)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

#Returns entire Owners table
def get_owner(db: Session):
    return db.query(models.Owner).all()

#Adds a owner to the Owners tabls
def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(name=owner.name, paid=owner.paid)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

#Joins Dogs and Owners tables where Owner.name == Dog.owner
def get_dog_owner(db:Session):
    db_dog_and_owner = db.query(models.Owner, models.Dog).filter(models.Owner.name == models.Dog.owner).all()
    return db_dog_and_owner

def create_payment(db: Session, payment: schemas.PayCreate):
    db_payment = models.Payments(name=payment.name, amount=payment.amount)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db:Session):
    return db.query(models.Payments).all()

def get_payment_by_name(db:Session, user_name:str):
    return db.query(models.Payments).filter(user_name == models.Payments.name).all()

def get_all_data_by_name(db:Session, user_name:str):
    return db.query(models.Payments, models.Owner, models.Dog).filter(
        models.Owner.name == user_name,
        models.Payments.name == user_name,
        models.Dog.owner == user_name).all()

def get_all(db:Session):
    return (db.query(models.Owner).all(), db.query(models.Dog).all(), db.query(models.Payments).all())