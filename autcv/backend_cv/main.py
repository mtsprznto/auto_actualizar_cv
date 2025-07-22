from fastapi import FastAPI
from fastapi.responses import JSONResponse
from cv.generarCv import generar_cv




from models.PropuestaInput import PropuestaInput

from utils.obtener_proyectos_actualizados import obtener_proyectos_actualizados

from ia.preguntar import seleccionar_proyectos

app = FastAPI()


username = "mtsprznto"

"""
GET
"""
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/repos-actualizados")
async def obtener_repos():
    """
    Obtiene los proyectos actualizados de GitHub para un usuario específico.
    """
    # proyectos_pre
    
    proyectos = await obtener_proyectos_actualizados(username)

    return JSONResponse(content=proyectos)




"""
POST
"""
@app.post("/propuesta")
async def recibir_propuesta(payload: PropuestaInput):
    """
    Recibe una propuesta laboral y devuelve una lista de proyectos seleccionados.
    """
    # proyectos seleccionados
    # aqui viene groq
    proyectos = await obtener_proyectos_actualizados(username)
    
    proyectos_seleccionados = seleccionar_proyectos(proyectos, payload.normalizada())
    
    generar_cv(proyectos_seleccionados)
    
    return JSONResponse(content=proyectos_seleccionados)
