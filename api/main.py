from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from typing import List, Dict
from .models.proyecto import Proyecto
from .utils.loader import cargar_proyectos_json






app = FastAPI(
    title="API Portafolio de Proyectos",
    description="Devuelve proyectos seleccionados desde JSON",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 para desarrollo. En producción puedes especificar ["https://tusitio.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.get("/", response_model=Dict[str, str])
def obtener_proyectos():
    """Devuelve un mensaje de bienvenida"""
    return {"message": "Bienvenido a la API de Proyectos ir a /docs para ver la documentacion"}

@app.get("/proyectos", response_model=List[Proyecto])
def obtener_proyectos():
    """Devuelve todos los proyectos"""
    return cargar_proyectos_json()

@app.get("/proyectos/{nombre}", response_model=Proyecto)
def obtener_proyecto_por_nombre(nombre: str):
    """Devuelve un proyecto por nombre"""
    proyectos = cargar_proyectos_json()
    for p in proyectos:
        if p.repositorio.lower() == nombre.lower():
            return p
    raise HTTPException(status_code=404, detail=f"Proyecto '{nombre}' no encontrado.")


#IMPORTANTE:
"""
Dejar esta funcion comentada ya que solo sirve en local y en produccion no se puede usar
"""


#from .utils.screenshot import obtener_screenshot

# @app.get("/preview")
# async def generar_previews():
#     """Genera y guarda screenshots de todos los proyectos con sitio_web"""
#     proyectos = cargar_proyectos_json()
#     capturados = []
#     for p in proyectos:
#         if p.sitio_web:
#             try:
#                 print(p.sitio_web)
#                 ruta = await obtener_screenshot(str(p.sitio_web), p.repositorio)
#                 capturados.append({
#                     "repositorio": p.repositorio,
#                     "ruta": ruta
#                 })
#             except Exception as e:
#                 capturados.append({
#                     "repositorio": p.repositorio,
#                     "error": str(e)
#                 })
#     return {"total": len(capturados), "resultados": capturados}


