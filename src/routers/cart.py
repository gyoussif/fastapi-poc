from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db

from .. import models, schemas

cart_router = APIRouter(prefix="/api/v1/cart", tags=["Carts"])


@cart_router.get("/")
async def list_carts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Cart).offset(skip).limit(limit).all()


@cart_router.get("/{cart_id}/")
async def get_cart_details(cart_id: int, db: Session = Depends(get_db)):
    return db.query(models.Cart).filter(models.Cart.id == cart_id).first()


@cart_router.get("/customer/{customer_id}/")
async def get_customer_carts(customer_id: int,
                             skip: int = 0,
                             limit: int = 10,
                             db: Session = Depends(get_db)):
    return db.query(models.Cart).filter(models.Cart.customer_id ==
                                        customer_id).offset(skip).limit(limit).all()


@cart_router.post("/")
def create_cart(cart_data: schemas.CartCreate, db: Session = Depends(get_db)):
    cart = models.Cart(**cart_data.dict())
    db.add(cart)
    db.commit()
    return cart


@cart_router.put("/{cart_id}/")
async def update_cart(cart_id: int, cart_data: schemas.CartUpdate, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    for key, value in cart_data.dict().items():
        setattr(cart, key, value)
    db.commit()
    db.refresh(cart)
    return cart


@cart_router.delete("/{cart_id}/")
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    db.delete(cart)
    db.commit()
    return {"ok": True}
