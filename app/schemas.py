from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime



class UserCreate(BaseModel):
    username: str
    password: str
    role: str  

class UserOut(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode = True


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemOut(MenuItemBase):
    id: int

    class Config:
        orm_mode = True



class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItem]

class OrderOut(BaseModel):
    id: int
    user_id: int
    items: List[OrderItem]
    created_at: datetime

    class Config:
        orm_mode = True



class BookingCreate(BaseModel):
    time: datetime

class BookingOut(BaseModel):
    id: int
    user_id: int
    time: datetime

    class Config:
        orm_mode = True
