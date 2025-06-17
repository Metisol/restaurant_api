from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database
from ..auth import get_current_user, require_role

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.BookingResponse)
def book_table(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("customer"))
):
    new_booking = models.Booking(
        user_id=current_user.id,
        time=booking.time,
        number_of_people=booking.number_of_people
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


@router.get("/", response_model=List[schemas.BookingResponse])
def get_own_bookings(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("customer"))
):
    return db.query(models.Booking).filter(models.Booking.user_id == current_user.id).all()


@router.get("/all", response_model=List[schemas.BookingResponse])
def get_all_bookings(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role("manager"))
):
    return db.query(models.Booking).all()
