# test-fastapi-container

API de ejemplo para gestionar gastos con FastAPI y SQLite.

Cómo usar:

- Instalar dependencias:

```bash
pip install -r requirements.txt
```

- Ejecutar localmente:

```bash
uvicorn main:app --reload
```

- Ejecutar tests:

```bash
pytest -q
```

- Construir imagen Docker (local):

```bash
docker build -t gastos-api:latest .
```

Para publicar en un registry, etiquetar y hacer push según su provider (Docker Hub, GHCR, ECR, ...).
# test-fastapi-container