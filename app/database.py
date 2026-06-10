import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dosya yolunu projenin kök dizinine göre dinamik olarak ayarlıyoruz
# Bu sayede veritabanı dosyası her zaman doğru klasörde oluşur
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'spender.db')}"

# SQLite bağlantısı için 'check_same_thread' parametresi şart
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()