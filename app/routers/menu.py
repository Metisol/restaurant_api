from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database
from ..auth import get_current_user, require_role

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

# Dependency for DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all menu items (open to all users)
@router.get("/", response_model=List[schemas.MenuItemResponse])
def get_menu_items(db: Session = Depends(get_db)):
    return db.query(models.MenuItem).all()

# Create a menu item (manager only)
@router.post("/", response_model=schemas.MenuItemResponse)
def create_menu_item(
    menu_item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("manager"))
):
    db_item = db.query(models.MenuItem).filter(models.MenuItem.name == menu_item.name).first()
    if db_item:
        raise HTTPException(status_code=400, detail="Menu item with this name already exists")
    new_item = models.MenuItem(**menu_item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Update a menu item (manager only)
@router.put("/{item_id}", response_model=schemas.MenuItemResponse)
def update_menu_item(
    item_id: int,
    menu_item: schemas.MenuItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("manager"))
):
    db_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for key, value in menu_item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete a menu item (manager only)
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("manager"))
):
    db_item = db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(db_item)
    db.commit()
    return
