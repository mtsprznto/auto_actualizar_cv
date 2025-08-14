from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from cv.generarCv import generar_cv


from models.PropuestaInput import PropuestaInput
from models.PreguntaInput import PreguntaInput

from utils.obtener_proyectos_actualizados import obtener_proyectos_actualizados, anadir_readme_proyectos_seleccionados
from utils.utils import preparar_readme_para_modelo

from ia.preguntar import seleccionar_proyectos, responder_propuesta, generar_experiencia_desde_readme


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
        "https://autcv.vercel.app",
        "http://localhost:3000",
        "https://autcv.mtsprz.org"
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
        
        # aqui se genera con groq (IA)
        proyectos_seleccionados = seleccionar_proyectos(proyectos, payload.normalizada())
        #print("Proyectos seleccionados:", proyectos_seleccionados)
        
        #obtener readme raw
        proyectos_seleccionados_readme = await anadir_readme_proyectos_seleccionados(username, proyectos_seleccionados)
        
        
        for proyecto in proyectos_seleccionados_readme:
            proyecto["readme_raw"] = preparar_readme_para_modelo(proyecto["readme_raw"])

        #print("PROYECTOS ENRIQUECIDOS: ",proyectos_seleccionados_readme)
        # Objetivo: es pasarle a un agente y que me seleccione las palabras claves dependiendo de la propuesta ingresada
        experiencias_cv = generar_experiencia_desde_readme(payload.normalizada(), proyectos_seleccionados_readme)
        for proyecto, experiencia in zip(proyectos_seleccionados_readme, experiencias_cv):
            proyecto["experiencia_cv"] = experiencia["experiencia_cv"]
            proyecto["keywords_detectadas"] = experiencia["keywords_detectadas"]
        print("EXPERIENCIAS CV: ",experiencias_cv)


        #print(proyectos_seleccionados)
        url_pdf = await generar_cv(proyectos_seleccionados,experiencias_cv ,"CV_Matias_Perez_Nauto.pdf")
        
        return JSONResponse(content={
            "cv_url": url_pdf
        })
    except Exception as e:
        print("❌ ERROR INTERNO:", str(e))
        return JSONResponse(status_code=500, content={"error": "Fallo interno en propuesta"})



@app.post("/responder")
async def recibir_pregunta(payload: PreguntaInput):
    """
    Recibe preguntas sobre propuesta laboral y devuelve una respueta adecuada a la propuesta laboral.
    """
    try:
        print(payload.pregunta)
        proyectos = await obtener_proyectos_actualizados(username)
        respuestas = responder_propuesta(proyectos=proyectos, pregunta=payload.pregunta)

        return JSONResponse(content={
            "respuestas": respuestas
        })
        
        
    except Exception as e:
        print("❌ ERROR INTERNO:", str(e))
        return JSONResponse(status_code=500, content={"error": "Fallo interno en responder"})