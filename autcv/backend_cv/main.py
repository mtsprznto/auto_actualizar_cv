from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from cv.generarCv import generar_cv


from models.PropuestaInput import PropuestaInput

from utils.obtener_proyectos_actualizados import obtener_proyectos_actualizados

from ia.preguntar import seleccionar_proyectos

origins = [
    "http://localhost:3000",                # Desarrollo local
    "https://autcv.vercel.app",             # Producción en Vercel
    "https://autcv.vercel.app/",            # Producción en Vercel
    "https://tu-dominio-custom.com",        # (opcional) si tenés otro dominio
]

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://autcv.vercel.app"
    ],         # Puedes usar ["*"] si querés permitir todo (no recomendado para producción)
    allow_credentials=True,
    allow_methods=["*"],                    # ["GET", "POST", ...] si querés limitar
    allow_headers=["*"],                    # ["Content-Type", "Authorization", ...]
)




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
    try:
        # proyectos seleccionados
        # aqui viene groq
        proyectos = await obtener_proyectos_actualizados(username)
        
        proyectos_seleccionados = seleccionar_proyectos(proyectos, payload.normalizada())
        print("Proyectos seleccionados:", proyectos_seleccionados)
        
        url_pdf = await generar_cv(proyectos_seleccionados, "CV_Matias_Perez_Nauto.pdf")
        
        return JSONResponse(content={
            "cv_url": url_pdf
        })
    except Exception as e:
        print("❌ ERROR INTERNO:", str(e))
        return JSONResponse(status_code=500, content={"error": "Fallo interno en propuesta"})


