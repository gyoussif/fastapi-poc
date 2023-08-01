from enum import Enum
from pydantic import BaseModel
from typing import Optional


# class Cart_Status(str, Enum):
#     IN_PROGRESS = "In Progress"
#     PROCESSING = "Processing"


class Cart(BaseModel):
    id: int
    customer_id: Optional[int] = None
    is_guest: bool
    # status: Cart_Status

# Pydantic model for creating a new Cart (POST request)
class CartCreate(BaseModel):
    customer_id: int
    is_guest: bool
    # status: Cart_Status

# Pydantic model for updating an existing Cart (PUT request)
class CartUpdate(BaseModel):
    customer_id: Optional[int] = None
    is_guest: Optional[bool] = None
    # status: Optional[Cart_Status] = None