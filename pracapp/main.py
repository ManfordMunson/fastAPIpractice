from cgitb import html
import json
from pyexpat import model
from sqlite3 import dbapi2
from unicodedata import name
from urllib import request, response
from urllib.request import Request
from fastapi import Depends, FastAPI, Form, Request
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from . import crud, models, schemas
from . database import SessionLocal, engine

#Creates all from the engine
models.Base.metadata.create_all(bind=engine)

#Launches the app
app = FastAPI()

#Yields the db and closes at finish
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.mount("/pracapp/static", StaticFiles(directory="pracapp/static"), name="static")
templates = Jinja2Templates(directory="pracapp/templates")

@app.get("/all/")
async def get_all(request:Request, db:Session=Depends(get_db)):
    title = "All Data"
    data = jsonable_encoder(crud.get_all(db=db))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

@app.get("/all/{name}")
async def get_all_data_by_name(name: str, request:Request, db: Session=Depends(get_db)):
    title = f"{name} - All Data by Name"
    data = jsonable_encoder(crud.get_all_data_by_name(db=db, user_name=name))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

@app.post("/payments/", response_model=schemas.Pay)
async def create_payment(payment: schemas.PayCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)

@app.get("/payments/", response_model= list[schemas.Pay])
async def get_all_payments(request:Request, db: Session=Depends(get_db)):
    title = "All Payements"
    data = jsonable_encoder(crud.get_payment(db=db))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

@app.get("/payments/{name}", response_model = list[schemas.Pay])
async def get_payments(name, request: Request, db: Session=Depends(get_db)):
    title = f"{name} - Payements"
    data = jsonable_encoder(crud.get_payment_by_name(db=db,user_name=name))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

#Creates a owner
@app.post("/owners/", response_model=schemas.Owner)
async def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return crud.create_owner(db=db, owner=owner)

#Gets all owners
@app.get("/owners/", response_model=list[schemas.Owner])
async def read_owner(request: Request, db: Session=Depends(get_db)):
    title = "Owners"
    data = jsonable_encoder(crud.get_owner(db=db))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

#Creates a dog
@app.post("/dogs/",response_model=schemas.Dog)
async def create_dog(dog: schemas.DogCreate, db:Session = Depends(get_db)):
    return crud.create_dog(db=db, dog=dog)

#Gets all dogs
@app.get("/dogs/", response_model=list[schemas.Dog])
async def read_dog(request: Request, db: Session=Depends(get_db)):
    title = "Dogs"
    data = jsonable_encoder(crud.get_dog(db=db))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

#Gets dogs and owners joined
@app.get("/owners_dogs/", response_class=HTMLResponse)
async def join_dog_owner(request: Request, db: Session=Depends(get_db)):
    title = "Dogs and Owners"
    data = jsonable_encoder(crud.get_dog_owner(db=db))
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title, "data":data})

#Home page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session=Depends(get_db)):
    title = "Home Page"
    return templates.TemplateResponse("homepage.html", {"request":request, "title":title})