from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, database, schemas
from fastapi.responses import HTMLResponse

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

# 1. POST /auth/register: User registration
@app.post("/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return {"message": "Kullanıcı başarıyla kaydedildi"}

# 2. POST /auth/login: JWT-based login
@app.post("/auth/login")
def login(user: schemas.UserLogin):
    return {"access_token": "token_buraya_gelecek"}

# 3. POST /items: Expense add
@app.post("/items")
def create_expense(expense: schemas.ExpenseCreate):
    return {"message": "Gider eklendi"}

# 4. GET /items/{id}: Expense display
@app.get("/items/{id}")
def read_expense(id: int):
    return {"item_id": id, "title": "Örnek Gider"}

# 5. PUT /items/{id}: Expence update
@app.put("/items/{id}")
def update_expense(id: int, expense: schemas.ExpenseCreate):
    return {"message": f"Gider {id} güncellendi"}

# 6. DELETE /items/{id}: Expense delete
@app.delete("/items/{id}")
def delete_expense(id: int):
    return {"message": f"Gider {id} silindi"}

# Bonus: Cross-user / Admin işlemi
@app.get("/admin/users")
def get_all_users():
    return {"users": ["admin_user", "test_user"]}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h1>Spender API'sine Hoş Geldiniz</h1>
            <p>Phase 1 başarıyla tamamlandı.</p>
            <p>API Dokümantasyonuna erişmek için tıklayın: 
                <a href="http://127.0.0.1:8000/docs">Swagger UI (Docs)</a>
            </p>
        </body>
    </html>
    """

print("\n" + "="*60)
print("Spender API Link: http://127.0.0.1:8000/docs")
print("="*60 + "\n")