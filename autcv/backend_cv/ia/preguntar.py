
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))


from ia.connect import get_groq_client
import json





def seleccionar_proyectos(proyectos: list, propuesta: str = "No especificada") -> str:
    """
    Analiza una lista completa de proyectos y genera una selección recomendada
    para mostrar en el CV según la propuesta dada.
    """
    client = get_groq_client()


    # Preparamos los proyectos en formato texto para el modelo
    # proyectos_texto = "\n".join([
    #     f"- {p['titulo']} ({p['lenguaje']}): {p['descripcion']}"
    #     for p in proyectos
    # ])


    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente técnico especializado en selección de proyectos para currículums. "
                "Tu tarea es analizar una propuesta laboral y devolver una lista en formato JSON con los proyectos más relevantes "
                "para mostrar en el CV. Usa exclusivamente el formato original que se te proporciona, sin modificar los campos ni agregar nuevos. "
                "Tu única salida debe ser un array JSON con los objetos seleccionados, sin explicaciones ni texto adicional."
            )
        },
        {
            "role": "user",
            "content": (
                f"Propuesta laboral:\n{propuesta}\n\n"
                f"Lista de proyectos (estructura original):\n{json.dumps(proyectos, ensure_ascii=False, indent=2)}\n\n"
                "Selecciona los más relevantes para incluir en el CV y devuélvelos en formato JSON."
            )
        }
    ]




    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # adaptá a tu modelo disponible
            messages=messages
        )
        raw_output = chat_completion.choices[0].message.content.strip()
        proyectos_seleccionados = json.loads(raw_output)
        return proyectos_seleccionados
    except Exception as e:
        print(f"❌ Error al generar CV adaptado: {e}")
        return "No se pudo adaptar el CV correctamente."



def responder_propuesta(proyectos: list, pregunta: str)-> str:
    """
    Recibe preguntas sobre propuesta laboral y responde en base a los proyectos que se entregan
    """
    client = get_groq_client()
    
    año_inicio_programacion = "2024"
    
    
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente técnico especializado en construir respuestas laborales personalizadas para postulantes en Latinoamérica. "
                "Tu tarea es analizar preguntas relacionadas a propuestas laborales y responder en primera persona, como si el postulante estuviera hablando directamente. "
                "Tenés que basarte en los proyectos entregados por el usuario, considerando su historial técnico, las tecnologías utilizadas y la duración de cada trabajo. "
                "Adaptá el lenguaje al contexto profesional de Chile y países hispanohablantes, incluyendo rangos salariales si aplica. "
                "La respuesta debe ser concreta, profesional y personalizada. Evitá generalidades, introducciones innecesarias o respuestas genéricas. "
                f"El usuario comenzó a programar en {año_inicio_programacion}. Considera esto para estimar su nivel de experiencia, responsabilidad técnica y expectativa salarial."
            )
        },
        {
            "role": "user",
            "content": (
                f"Pregunta:\n{pregunta}\n\n"
                f"Lista de proyectos (estructura original):\n{json.dumps(proyectos, ensure_ascii=False, indent=2)}\n\n"
                "Redactá la respuesta como si yo mismo la estuviera diciendo. "
                "Tené en cuenta mi experiencia técnica, el nivel que tengo hoy, y adaptá el tono a un contexto profesional chileno actual. "
                f"Tengo {2025 - int(año_inicio_programacion)} años de experiencia. Basate en eso para sugerir rangos salariales y responsabilidades acordes a un perfil junior o semi-senior. "
                "Si la pregunta está relacionada con remuneración, entregá una estimación mensual líquida realista en CLP."
            )
        }
    ]

    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # adaptá a tu modelo disponible
            messages=messages
        )
        raw_output = chat_completion.choices[0].message.content.strip()
        
        return raw_output
    except Exception as e:
        print(f"❌ Error al generar CV adaptado: {e}")
        return "No se pudo adaptar el CV correctamente."
