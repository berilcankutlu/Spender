from pydantic import BaseModel, ConfigDict
from typing import List


# 1. Token Şeması
class Token(BaseModel):
    access_token: str
    token_type: str


# 2. Harcama (Expense) Şemaları
class ExpenseBase(BaseModel):
    title: str
    amount: float


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int
    owner_id: int

    # Veritabanı modelleriyle uyum için
    model_config = ConfigDict(from_attributes=True)


# 3. Kullanıcı (User) Şemaları
class UserBase(BaseModel):
    username: str  # Veritabanındaki 'username' sütunuyla birebir eşleşmeli


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    expenses: List[Expense] = []

    # Veritabanı modelleriyle uyum için
    model_config = ConfigDict(from_attributes=True)