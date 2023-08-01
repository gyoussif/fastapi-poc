from sqlalchemy import Boolean, Column, Integer, String

from src.database import Base


class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String)
    is_guest = Column(Boolean, default=False)
