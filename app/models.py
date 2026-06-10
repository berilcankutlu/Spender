from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # Boolean kullanmak daha profesyonel bir yaklaşımdır
    is_admin = Column(Boolean, default=False)

    # Kullanıcının giderleri (silme işlemi gerçekleştiğinde giderler de silinir - cascade)
    expenses = relationship("Expense", back_populates="owner", cascade="all, delete-orphan")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    amount = Column(Float)

    owner_id = Column(Integer, ForeignKey("users.id"))

    # Giderin sahibi ile olan ilişki
    owner = relationship("User", back_populates="expenses")