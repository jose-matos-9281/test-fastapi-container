import os
from pathlib import Path

# Usar DB en archivo temporal para tests (más fiable que memory con múltiples conexiones)
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_gastos.db")

from fastapi.testclient import TestClient
import main


client = TestClient(main.app)


def test_crud_gasto():
    # Crear gasto
    payload = {"concepto": "Café", "monto": 2.5, "categoria": "Alimentación"}
    r = client.post("/gastos", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["concepto"] == "Café"
    gasto_id = data["id"]

    # Obtener gasto
    r = client.get(f"/gastos/{gasto_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == gasto_id

    # Actualizar gasto
    r = client.put(f"/gastos/{gasto_id}", json={"monto": 3.0})
    assert r.status_code == 200
    data = r.json()
    assert data["monto"] == 3.0

    # Listar gastos
    r = client.get("/gastos")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert any(g["id"] == gasto_id for g in data)

    # Borrar gasto
    r = client.delete(f"/gastos/{gasto_id}")
    assert r.status_code == 204

    # Confirmar borrado
    r = client.get(f"/gastos/{gasto_id}")
    assert r.status_code == 404

    # limpiar fichero de pruebas si existe
    db_file = Path("./test_gastos.db")
    if db_file.exists():
        try:
            db_file.unlink()
        except Exception:
            pass
