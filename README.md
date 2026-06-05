# 💸 Spender - Personal Expense Tracking App

Spender is a modern and scalable personal finance application based on FastAPI that allows users to securely track their expenses.
* SE457 Secure Software Development
* Deniz Özçelik, Berilcan Kutlu 

## 🚀 Features
* Secure Authentication: Secure login/logout transactions based on JWT.

* Data Privacy: Passwords are hashed using bcrypt.

* 3-Tier Architecture: Professional and sustainable code structure.

* Database Relationships: User-based, personal expense management.

* Fast API: High-performance endpoints with FastAPI.

## 🛠 Technologies Used
* Framework: FastAPI

* Database: SQLAlchemy (SQLite)

* Security: Passlib, PyJWT

* Server: Uvicorn

## ⚙️ Installation
1. **Clone the repository:**
```bash
git clone https://github.com/berilcankutlu/Spender.git
cd Spender
```
2. **Upload the addictions:**
```bash
pip install -r requirements.txt
```
3. **Access the documentation:**

After launching the application, you can test your API by going to http://127.0.0.1:8000/docs in your browser.

## 📁 Project Structure
```bash
Spender/
├── app/
│ ├── __init__.py
│ ├── main.py # Entry point and API endpoints
│ ├── auth.py # Security and JWT logic
│ ├── models.py # SQLAlchemy database models
│ ├── schemas.py # Pydantic schemas
│ └── database.py # Database connection management
├── requirements.txt # Library list
└── README.md # Project documentation           
```