import json
from pathlib import Path
from typing import List
from ..models.proyecto import Proyecto

def cargar_proyectos_json(ruta: str = "./data/proyectos_combinados_all.json") -> List[Proyecto]:
    """Carga los proyectos desde un archivo JSON"""
    ruta_archivo = Path(ruta)
    if not ruta_archivo.exists():
        return []

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        data = json.load(f)

    proyectos = []
    for p in data:
        if p.get("sitio_web") == "":
            p["sitio_web"] = None
        proyectos.append(Proyecto(**p))
    
    return proyectos
