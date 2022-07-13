from typing import Any
from sqlalchemy.orm import Session
from . import models, schemas


def get_dogs_per_owner(db: Session, name: str) -> list:
    """Returns all dogs associated with the user"""
    owner_of_dogs = db.query(models.Owner).filter(models.Owner.name == name).one()
    return owner_of_dogs.dogs


def get_dog(db: Session) -> list:
    """Returns the entire Dog table."""
    return db.query(models.Dog).all()


def create_dog(
    db: Session, name: str, age: int, breed: str, owner_id: int
) -> schemas.Dog:
    """Adds a Dog to the table."""
    db_dog = models.Dog(name=name, breed=breed, age=age, owner_id=owner_id)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog


def get_owner(db: Session) -> list:
    """Returns the entire Owner table."""
    return db.query(models.Owner).all()


def create_owner(db: Session, name, paid) -> schemas.Owner:
    """Adds a Owner to the table."""
    db_owner = models.Owner(name=name, paid=paid)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def get_dog_owner(db: Session, owner_name) -> list[tuple]:
    """Joins Dog and Owner table a specified name."""
    return (
        db.query(models.Owner, models.Dog)
        .filter(models.Owner.name == owner_name, models.Dog.owner == models.Owner.name)
        .all()
    )


def create_payment(db: Session, name, amount) -> schemas.Pay:
    """Adds a Payment to the table."""
    db_payment = models.Payments(name=name, amount=amount)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def del_owner(db: Session, id) -> Any:
    """Deletes a payment from the Payment table."""
    db_owner_delete = db.query(models.Owner).filter(models.Owner.id == id).one()
    db.delete(db_owner_delete)
    db.commit()
    return db_owner_delete


def get_payment(db: Session) -> list:
    """Returns the entire Payment table."""
    return db.query(models.Payments).all()


def get_payment_by_name(db: Session, name: str) -> list:
    """Returns all payments under a specific name."""
    return db.query(models.Payments).filter(name == models.Payments.name).all()


def get_all_data_by_name(db: Session, user_name: str) -> list[tuple]:
    """Returns all data under a specified name."""
    return (
        db.query(models.Payments, models.Owner, models.Dog)
        .filter(
            models.Owner.name == user_name,
            models.Payments.name == user_name,
            models.Dog.owner == user_name,
        )
        .all()
    )


def get_all(db: Session) -> tuple[list, list, list]:
    """Gets all data in all tables."""
    return (
        db.query(models.Owner).all(),
        db.query(models.Dog).all(),
        db.query(models.Payments).all(),
    )


def update_pay(db: Session, payment_id, new_payment) -> Any:
    """Updates a payment by ID."""
    payment2update = (
        db.query(models.Payments)
        .filter(models.Payments.id == payment_id)
        .update({"amount": new_payment})
    )
    db.commit()
    return payment2update


def remove_pay(db: Session, payment_id) -> Any:
    """Removes a payment from Payment table by ID."""
    payment2delete = (
        db.query(models.Payments).filter(models.Payments.id == payment_id).one()
    )
    db.delete(payment2delete)
    db.commit()
    return payment2delete
