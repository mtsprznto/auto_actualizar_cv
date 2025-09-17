
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


def generar_experiencia_desde_readme(propuesta: str, proyectos: list) -> list:
    """
    Genera experiencias profesionales adaptadas al CV usando los README
    y alineadas con la propuesta laboral.
    """
    client = get_groq_client()



    messages = [
        {
            "role": "system",
            "content": (
                "Eres un experto en redacción de currículums técnicos. "
                "Tu tarea es leer el README de cada proyecto y generar una experiencia profesional adaptada al CV, alineada con la propuesta laboral. "
                "Extrae palabras clave relevantes y redacta una descripción profesional, clara y orientada al impacto. "
                "Devuelve un array JSON con: 'titulo', 'experiencia_cv', 'keywords_detectadas'. "
                "No incluyas explicaciones ni texto adicional fuera del JSON."
            )
        },
        {
            "role": "user",
            "content": (
                f"Propuesta laboral:\n{propuesta}\n\n"
                f"Proyectos con README:\n{json.dumps(proyectos, ensure_ascii=False, indent=2)}\n\n"
                "Devuélveme el array JSON con las experiencias adaptadas para el CV."
            )
        }
    ]

    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        raw_output = chat_completion.choices[0].message.content.strip()
        # 🧹 Eliminar delimitadores Markdown si existen
        if raw_output.startswith("```json"):
            raw_output = raw_output.replace("```json", "").strip()
        if raw_output.endswith("```"):
            raw_output = raw_output[:-3].strip()
        print("RAW RESPUESTA", raw_output)
        # 🧪 Intentar parsear
        try:
            experiencias_adaptadas = json.loads(raw_output)
            return experiencias_adaptadas
        except Exception as e:
            print("❌ JSON malformado. Contenido recibido:")
            print(raw_output)
            raise e

    except Exception as e:
        print(f"❌ Error al generar experiencias desde README: {e}")
        return []


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
