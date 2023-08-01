# main.py
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.database import engine, get_db

from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/api/v1/cart/")
async def list_carts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Cart).offset(skip).limit(limit).all()


@app.get("/api/v1/cart/{cart_id}/")
async def get_cart_details(cart_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cart).filter(models.Cart.id == cart_id).first()


@app.get("/api/v1/cart/customer/{customer_id}/")
async def get_customer_carts(customer_id: int,
                             skip: int = 0,
                             limit: int = 10,
                             db: Session = Depends(get_db)):
    return db.query(models.Cart).filter(models.Cart.customer_id ==
                                        customer_id).offset(skip).limit(limit).all()

# Endpoint to create a new Cart


@app.post("/api/v1/cart/")
def create_cart(cart_data: schemas.CartCreate, db: Session = Depends(get_db)):
    cart = models.Cart(**cart_data.dict())
    db.add(cart)
    db.commit()
    return cart

# Endpoint to update an existing Cart


@app.put("/api/v1/cart/{cart_id}/")
async def update_cart(cart_id: int, cart_data: schemas.CartUpdate, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    for key, value in cart_data.dict().items():
        setattr(cart, key, value)
    db.commit()
    db.refresh(cart)
    return cart


@app.delete("/api/v1/cart/{cart_id}/")
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    db.delete(cart)
    db.commit()
    return {"ok": True}
