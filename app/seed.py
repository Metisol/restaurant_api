from sqlalchemy.orm import Session
from . import models, database, auth
from datetime import datetime, timedelta

def seed_data():
    db: Session = database.SessionLocal()

    
    db.query(models.Booking).delete()
    db.query(models.OrderItem).delete()
    db.query(models.Order).delete()
    db.query(models.MenuItem).delete()
    db.query(models.User).delete()
    db.commit()

    
    user1 = models.User(
        username="customer1",
        hashed_password=auth.get_password_hash("password123"),
        role="customer"
    )
    user2 = models.User(
        username="manager1",
        hashed_password=auth.get_password_hash("password123"),
        role="manager"
    )
    user3 = models.User(
        username="admin1",
        hashed_password=auth.get_password_hash("password123"),
        role="admin"
    )

    db.add_all([user1, user2, user3])
    db.commit()

    
    item1 = models.MenuItem(name="Margherita Pizza", description="Classic cheese pizza", price=10.99)
    item2 = models.MenuItem(name="Spaghetti Carbonara", description="Pasta with bacon and cheese", price=12.99)
    item3 = models.MenuItem(name="Caesar Salad", description="Fresh romaine with dressing", price=8.99)

    db.add_all([item1, item2, item3])
    db.commit()

    
    booking1 = models.Booking(user_id=user1.id, time=datetime.utcnow() + timedelta(days=1))
    booking2 = models.Booking(user_id=user1.id, time=datetime.utcnow() + timedelta(days=2))

    db.add_all([booking1, booking2])
    db.commit()

    print("Database seeded with test data.")
    db.close()

if __name__ == "__main__":
    seed_data()
