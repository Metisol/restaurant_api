 🍽️ Restaurant API

A RESTful API for managing a restaurant system, built with **FastAPI**. The API supports JWT-based authentication and role-based access control for **Customers**, **Managers**, and **Admins**.

Features

- 🔐 JWT Authentication
- 👥 Role-based Access Control:
  - **Admin**: Manage users, view analytics
  - **Manager**: Manage menus, view bookings and orders
  - **Customer**: Browse menus, place orders, view own bookings
- 📋 Menu Management (CRUD)
- 📦 Order Management
- 📅 Table Booking System
- 📊 Admin analytics endpoints (optional)
- 🧪 Built-in Swagger UI for testing endpoints



## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite (default), can be upgraded to PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **ORM**: SQLAlchemy
- **Password Hashing**: Passlib (bcrypt)
- **Documentation**: Auto-generated with Swagger UI

---

## 📦 Installation

### Clone the repo

```bash
git clone https://github.com/Metisol/restaurant_api.git
cd restaurant_api
