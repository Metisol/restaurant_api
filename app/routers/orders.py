from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database
from ..auth import get_current_user, require_role

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.OrderResponse)
def place_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("customer"))
):
    menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == order.menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    new_order = models.Order(
        user_id=current_user.id,
        menu_item_id=order.menu_item_id,
        quantity=order.quantity,
        status="Pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/", response_model=List[schemas.OrderResponse])
def get_orders(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("customer"))
):
    return db.query(models.Order).filter(models.Order.user_id == current_user.id).all()
