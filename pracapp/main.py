from types import GeneratorType
from typing import Any
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db() -> GeneratorType:
    """Opens the connection to the Database and then closes at completion."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.delete("/payments/{payment_id}")
async def drop_payments(payment_id: int, db: Session = Depends(get_db)) -> Any:
    """Delete existing payment from system.

    ARGS: {
     payment_id: int = ID used to lookup payments from the table
     db: Session = Active sesion connection made with the Database
    }
    """
    return crud.remove_pay(db=db, payment_id=payment_id)


@app.put("/payments/{payment_id}")
async def update_payments(
    payment_id: int, new_payment: float, db: Session = Depends(get_db)
) -> Any:
    """Updates existing payment in the system.

    ARGS: {
        payment_id: int = ID used lookup payments from the tables
        new_payment: float = Value assigned as payment in the Database
        db: Session = Active session connection made with the Database
    }
    """
    return crud.update_pay(db=db, payment_id=payment_id, new_payment=new_payment)


@app.post("/payments/")
async def create_payment(
    name: str, amount: float, db: Session = Depends(get_db)
) -> schemas.Pay:
    """Creates a new payment in the system.

    ARGS: {
        name: str = Name payments are assigned to
        amount: float = Value assigned to the payment
        db: Session = Active session connection made with the Database
    }
    """
    return crud.create_payment(db=db, name=name, amount=amount)


@app.get("/payments/")
async def get_all_payments(db: Session = Depends(get_db)) -> list:
    """Gets all payments currently in the system.

    ARGS: {
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_payment(db=db)


@app.get("/payments/{name}")
async def get_payments(name: str, db: Session = Depends(get_db)) -> list:
    """Gets all payments under a specified name.

    ARGS: {
        name: str = Value used to lookup in the Database
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_payment_by_name(db=db, name=name)


@app.get("/all/")
async def get_all(db: Session = Depends(get_db)) -> tuple[list]:
    """Gets all data from all tables in the system.

    ARGS: {
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_all(db=db)


@app.get("/all/{name}")
async def get_all_data_by_name(name: str, db: Session = Depends(get_db)) -> list[tuple]:
    """Gets all data from all datas correlated with a specific name.

    ARGS: {
        name: str = Value to get all data by in the Database
        db: Session = Active session connection made with the Database
    }
    """

    return crud.get_all_data_by_name(db=db, user_name=name)


@app.delete("/owners/{id}")
async def delete_owners(id: int, db: Session = Depends(get_db)) -> Any:
    """Deletes an existing Owner from the system.

    ARGS: {
        id: int = ID to delete rows by in Database
        db: Session = Active session connection made with the Database
    }
    """
    return crud.del_owner(db=db, id=id)


@app.post("/owners/")
async def create_owner(
    name: str, paid: bool, db: Session = Depends(get_db)
) -> schemas.Owner:
    """Creates a new Owner in the system.

    ARGS: {
        name: str = Owners name in Database
        paid: bool = If the owner is current on payments
        db: Session = Active session connection made with the Database
    }
    """
    return crud.create_owner(db=db, name=name, paid=paid)


@app.get("/owners/")
async def read_owner(db: Session = Depends(get_db)) -> list:
    """Gets all owners currently in the system.

    ARGS: {
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_owner(db=db)


@app.post("/dogs/")
async def create_dog(
    name: str, breed: str, age: int, owner_id: int, db: Session = Depends(get_db)
) -> schemas.Dog:
    """Creates a new Dog in the system.

    ARGS: {
        name: str = Name assigned to Dog
        breed: str = Breed of the Dog
        age: int = Age of the Dog
        owner_id: int = Owners ID used to form a relationships
        db: Session = Active session connection made with the Database
    }
    """

    return crud.create_dog(db=db, name=name, breed=breed, age=age, owner_id=owner_id)


@app.get("/dogs/")
async def read_dog(db: Session = Depends(get_db)) -> list:
    """Gets all dogs currently in the system.

    ARGS: {
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_dog(db=db)


@app.delete("/dogs/")
async def delete_dog(id: int, db: Session = Depends(get_db)) -> Any:
    """Deletes a dog based on ID of the dog.

    ARGS: {
        id: int = ID used to lookup dog in the Database
        db: Session = Active session connection made with the Database
    }
    """
    return crud.del_dog(db=db, id=id)


@app.get("/owners_dogs/{owner_name}")
async def join_dog_owner(owner_name: str, db: Session = Depends(get_db)) -> list[tuple]:
    """Joins the Dog and Owner tables on Name.

    ARGS: {
        owner_name: str = Owner Name to lookup all dogs associated with it in the Database
        db: Session = Active session connection made with the Database
    }
    """
    return crud.get_dogs_per_owner(db=db, name=owner_name)


@app.get("/")
async def read_root() -> dict:
    """Home Page return."""
    return {"Hello": "World"}
