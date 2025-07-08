from fastapi import APIRouter, HTTPException
from typing import List
from models.proyecto import Proyecto
from utils.loader import cargar_proyectos_json

router = APIRouter(
    prefix="/proyectos",
    tags=["Proyectos"]
)

@router.get("/", response_model=List[Proyecto])
def obtener_proyectos():
    """Devuelve todos los proyectos"""
    return cargar_proyectos_json()

@router.get("/{nombre}", response_model=Proyecto)
def obtener_proyecto_por_nombre(nombre: str):
    """Devuelve un proyecto por nombre"""
    proyectos = cargar_proyectos_json()
    for p in proyectos:
        if p.repositorio.lower() == nombre.lower():
            return p
    raise HTTPException(status_code=404, detail=f"Proyecto '{nombre}' no encontrado.")
