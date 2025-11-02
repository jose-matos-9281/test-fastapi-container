import os
from sqlalchemy import Column, Integer, Float, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Permitir sobreescribir la URL de la base de datos mediante la variable de entorno DATABASE_URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./gastos.db")
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base para los modelos
Base = declarative_base()


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    concepto = Column(String, index=True)
    monto = Column(Float)
    fecha = Column(Date, default=date.today)
    categoria = Column(String)


# Crear las tablas (si no existen)
Base.metadata.create_all(bind=engine)