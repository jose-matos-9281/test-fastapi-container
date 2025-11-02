from pydantic import BaseModel
from typing import Optional
from datetime import date


class GastoBase(BaseModel):
    concepto: str
    monto: float
    fecha: Optional[date] = None
    categoria: Optional[str] = None


class GastoCreate(GastoBase):
    pass


class GastoUpdate(BaseModel):
    concepto: Optional[str] = None
    monto: Optional[float] = None
    fecha: Optional[date] = None
    categoria: Optional[str] = None


class GastoOut(GastoBase):
    id: int

    class Config:
        orm_mode = True
