from sqlalchemy.orm import Session
import models
import schemas


def get_gasto(db: Session, gasto_id: int):
    return db.query(models.Gasto).filter(models.Gasto.id == gasto_id).first()


def get_gastos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gasto).offset(skip).limit(limit).all()


def create_gasto(db: Session, gasto: schemas.GastoCreate):
    db_gasto = models.Gasto(
        concepto=gasto.concepto,
        monto=gasto.monto,
        fecha=gasto.fecha,
        categoria=gasto.categoria,
    )
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto


def update_gasto(db: Session, db_gasto: models.Gasto, gasto_update: schemas.GastoUpdate):
    for field, value in gasto_update.dict(exclude_unset=True).items():
        setattr(db_gasto, field, value)
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto


def delete_gasto(db: Session, db_gasto: models.Gasto):
    db.delete(db_gasto)
    db.commit()
