
from fastapi import FastAPI

import sys
from pathlib import Path

# Asegura que el directorio raíz quede en sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from routers import proyectos


app = FastAPI(
    title="API Portafolio de Proyectos",
    description="Devuelve proyectos seleccionados desde JSON",
    version="1.0.0"
)

app.include_router(proyectos.router)

handler = app