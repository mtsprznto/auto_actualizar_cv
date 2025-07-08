from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, List

class Proyecto(BaseModel):
    titulo: str
    descripcion: str
    fecha: str
    url: HttpUrl
    lenguaje: Optional[str]
    lenguajes_completos: Dict[str, int]
    topics: List[str]
    sitio_web: Optional[HttpUrl]
    repositorio: str