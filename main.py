def main():
    print("Hello from test-fastapi-container!")


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import crud


app = FastAPI(title="API de Gastos")


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/gastos", response_model=schemas.GastoOut, status_code=201)
def create_gasto(gasto: schemas.GastoCreate, db: Session = Depends(get_db)):
    return crud.create_gasto(db, gasto)


@app.get("/gastos", response_model=List[schemas.GastoOut])
def list_gastos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_gastos(db, skip=skip, limit=limit)


@app.get("/gastos/{gasto_id}", response_model=schemas.GastoOut)
def get_gasto(gasto_id: int, db: Session = Depends(get_db)):
    db_gasto = crud.get_gasto(db, gasto_id)
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return db_gasto


@app.put("/gastos/{gasto_id}", response_model=schemas.GastoOut)
def update_gasto(gasto_id: int, gasto: schemas.GastoUpdate, db: Session = Depends(get_db)):
    db_gasto = crud.get_gasto(db, gasto_id)
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    return crud.update_gasto(db, db_gasto, gasto)


@app.delete("/gastos/{gasto_id}", status_code=204)
def delete_gasto(gasto_id: int, db: Session = Depends(get_db)):
    db_gasto = crud.get_gasto(db, gasto_id)
    if not db_gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    crud.delete_gasto(db, db_gasto)
    return None
