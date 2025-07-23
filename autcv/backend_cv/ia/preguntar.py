
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
                "Tu tarea es analizar preguntas relacionadas a propuestas laborales y responder en base a los proyectos entregados por el usuario. "
                "Considera el historial técnico, el tipo de proyectos realizados y su duración. "
                "Adapta tus respuestas a valores de mercado y lenguaje profesional usado en Chile y otros países de habla hispana. "
                "Evita generalidades. Ofrece una respuesta concreta, clara y profesional. "
                "No hagas introducciones. Tu salida debe ser solamente la pregunta y la respuesta bien redactada."
                f"El usuario comenzó a programar en {año_inicio_programacion}. Considera esto al sugerir rangos salariales y nivel de responsabilidad técnica."
            )
        },
        {
            "role": "user",
            "content": (
                f"Pregunta :\n{pregunta}\n\n"
                f"Lista de proyectos (estructura original):\n{json.dumps(proyectos, ensure_ascii=False, indent=2)}\n\n"
                "Responde considerando los proyectos listados, la experiencia técnica reflejada en ellos y precios que se alineen con el mercado chileno actual."
                f"Ten en cuenta que el usuario comenzo en {año_inicio_programacion}. Sugiere rangos salariales acordes al mercado chileno actual para perfiles junior o semi-senior en roles similares."
                "Si la pregunta está relacionada con remuneración, entrega un rango estimado en CLP mensual líquido, basado en el perfil técnico y nivel de experiencia del usuario."
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
