from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import models, schemas, database

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# Veritabanı oturumu bağımlılığı
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Kullanıcı Kayıt
@app.post("/auth/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu kullanıcı zaten kayıtlı")

    new_user = models.User(username=user.username, hashed_password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 2. Gider Ekleme (Manuel/Yetkisiz Test Versiyonu)
@app.post("/expenses", response_model=schemas.Expense)
def create_expense(
        expense: schemas.ExpenseCreate,
        db: Session = Depends(get_db)
):
    # Test için owner_id'yi sabit 1 olarak veriyoruz
    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        owner_id=1
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


# 3. Giderleri Listeleme (Test Versiyonu)
@app.get("/expenses", response_model=list[schemas.Expense])
def read_expenses(db: Session = Depends(get_db)):
    # Tüm giderleri getiriyoruz
    return db.query(models.Expense).all()


# 4. Gider Silme
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Gider bulunamadı")
    db.delete(expense)
    db.commit()
    return {"message": "Harcama silindi"}


# 5. Admin İstatistik
@app.get("/admin/stats")
def get_stats(db: Session = Depends(get_db)):
    count = db.query(models.Expense).count()
    return {"total_expenses": count}


# 6. Kullanıcı Girişi
@app.post("/auth/login", response_model=schemas.Token)
def login():
    return {"access_token": "gizli-token", "token_type": "bearer"}