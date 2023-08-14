# from enum import Enum
from typing import Optional

from pydantic import BaseModel

class Cart(BaseModel):
    id: int
    customer_id: Optional[int] = None
    is_guest: bool

class CartCreate(BaseModel):
    customer_id: int
    is_guest: bool

class CartUpdate(BaseModel):
    customer_id: Optional[int] = None
    is_guest: Optional[bool] = None
