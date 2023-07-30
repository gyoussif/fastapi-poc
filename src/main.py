# main.py

from fastapi import FastAPI,Depends, Request,status
from sqlalchemy.orm import Session
from . import models
from src.database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
#Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root(request: Request, db: Session=Depends(get_db)):
    qs=db.query(models.Todo).all()
    return qs

@app.post("/add")
async def root(request: Request, db: Session=Depends(get_db)):
    qs=db.query(models.Todo).all()
    db.add(new_obj)
    db.commit()
    return qs