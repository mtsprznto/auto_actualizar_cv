from fastapi import FastAPI, HTTPException
from typing import List, Dict
from .models.proyecto import Proyecto
from .utils.loader import cargar_proyectos_json


app = FastAPI(
    title="API Portafolio de Proyectos",
    description="Devuelve proyectos seleccionados desde JSON",
    version="1.0.0"
)

@app.get("/", response_model=Dict[str, str])
def obtener_proyectos():
    """Devuelve todos los proyectos"""
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
