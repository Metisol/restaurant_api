

from fastapi import FastAPI
from .routers import users
from .database import engine
from .database import Base, engine
from . import models, database
from . import models

from .routers import users, menu, orders, bookings



models.Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Restaurant API",
    description="API for restaurant management with JWT-based auth and roles",
    version="1.0.0"
)
app.include_router(users.router)
app.include_router(menu.router)
app.include_router(orders.router)
app.include_router(bookings.router)




