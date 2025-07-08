import sys
import os
sys.path.append(os.path.dirname(__file__))


from fastapi import FastAPI
from routers import proyectos


app = FastAPI(
    title="API Portafolio de Proyectos",
    description="Devuelve proyectos seleccionados desde JSON",
    version="1.0.0"
)

app.include_router(proyectos.router)

handler = app