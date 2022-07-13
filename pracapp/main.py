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
    """Delete existing payment from system."""
    return crud.remove_pay(db=db, payment_id=payment_id)


@app.put("/payments/{payment_id}")
async def update_payments(
    payment_id: int, new_payment: float, db: Session = Depends(get_db)
) -> Any:
    """Updates existing payment in the system."""
    return crud.update_pay(db=db, payment_id=payment_id, new_payment=new_payment)


@app.post("/payments/")
async def create_payment(
    name: str, amount: float, db: Session = Depends(get_db)
) -> schemas.Pay:
    """Creates a new payment in the system."""
    return crud.create_payment(db=db, name=name, amount=amount)


@app.get("/payments/")
async def get_all_payments(db: Session = Depends(get_db)) -> list:
    """Gets all payments currently in the system."""
    return crud.get_payment(db=db)


@app.get("/payments/{name}")
async def get_payments(name: str, db: Session = Depends(get_db)) -> list:
    """Gets all payments under a specified name."""
    return crud.get_payment_by_name(db=db, name=name)


@app.get("/all/")
async def get_all(db: Session = Depends(get_db)) -> tuple[list]:
    """Gets all data from all tables in the system."""
    return crud.get_all(db=db)


@app.get("/all/{name}")
async def get_all_data_by_name(name: str, db: Session = Depends(get_db)) -> list[tuple]:
    """Gets all data from all datas correlated with a specific name."""
    return crud.get_all_data_by_name(db=db, user_name=name)


@app.delete("/owners/{id}")
async def delete_owners(id: int, db: Session = Depends(get_db)) -> Any:
    """Deletes an existing Owner from the system."""
    return crud.del_owner(db=db, id=id)


@app.post("/owners/")
async def create_owner(
    name: str, paid: bool, db: Session = Depends(get_db)
) -> schemas.Owner:
    """Creates a new Owner in the system."""
    return crud.create_owner(db=db, name=name, paid=paid)


@app.get("/owners/")
async def read_owner(db: Session = Depends(get_db)) -> list:
    """Gets all owners currently in the system."""
    return crud.get_owner(db=db)


@app.post("/dogs/")
async def create_dog(
    name: str, breed: str, age: int, owner_id: int, db: Session = Depends(get_db)
) -> schemas.Dog:
    """Creates a new Dog in the system."""
    return crud.create_dog(db=db, name=name, breed=breed, age=age, owner_id=owner_id)


@app.get("/dogs/")
async def read_dog(db: Session = Depends(get_db)) -> list:
    """Gets all dogs currently in the system."""
    return crud.get_dog(db=db)


@app.get("/owners_dogs/{owner_name}")
async def join_dog_owner(owner_name: str, db: Session = Depends(get_db)) -> list[tuple]:
    """Joins the Dog and Owner tables on Name."""
    return crud.get_dogs_per_owner(db=db, name=owner_name)


@app.get("/")
async def read_root() -> dict:
    """Home Page return."""
    return {"Hello": "World"}
