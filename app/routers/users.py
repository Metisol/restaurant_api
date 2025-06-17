

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, database, auth

router = APIRouter()


@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username taken")
    
    
    hashed = auth.get_password_hash(user.password)

    new_user = models.User(
        username=user.username,
        hashed_password=hashed,
        role=user.role  
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    
    
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    
    token = auth.create_access_token({"sub": user.username})
    
    return {"access_token": token, "token_type": "bearer"}
