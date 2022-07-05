from email.policy import HTTP
from pyexpat import model
from telnetlib import SE
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from . database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/owners/", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = crud.get_owner(db, name=owner.name)
    if db_owner:
        raise HTTPException(status_code=400, detail = "Name already registered")
    return crud.create_owner(db=db, owner=owner)


@app.get("/owners/", response_model=list[schemas.Owner])
def read_owner(skip: int = 0, limit: int = 100, db: Session=Depends(get_db)):
    owners = crud.get_owner(db, skip = skip, limit=limit)
    return owners

@app.post("/dogs/",response_model=schemas.Dog)
def create_dog(dog: schemas.DogCreate, db:Session = Depends(get_db)):
    db_dog = crud.get_dog(db)
    if db_dog:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_dog(db=db, dog=dog)

@app.get("/")
def read_root():
    return {"Hello":"World"}