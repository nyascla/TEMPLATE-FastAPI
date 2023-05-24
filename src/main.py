from fastapi import FastAPI
from .routes import items
from .database import engine

app = FastAPI()

# Crear las tablas en la base de datos
def create_tables():
    from .models import Base
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    create_tables()

# Registrar las rutas
app.include_router(items.router)

# Instalar dependencias
#
# pip install -r requirements.txt
#

#
# Levantar servidor
#
# uvicorn src.main:app --reload
# uvicorn src.main:app --host 192.168.1.133 --port 9876