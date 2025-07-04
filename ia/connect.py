import os
from dotenv import load_dotenv
from groq import Groq

# Cargar .env al arrancar
load_dotenv()

def get_groq_client() -> Groq:
    """
    Inicializa y devuelve el cliente Groq con validación robusta
    """
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or not api_key.strip():
        raise EnvironmentError("❌ GROQ_API_KEY no fue encontrado o está vacío en las variables de entorno.")

    try:
        client = Groq(api_key=api_key)
        return client
    except Exception as e:
        raise RuntimeError(f"⚠️ Error al inicializar el cliente Groq: {str(e)}")

# Cliente listo para usar
groq_client = get_groq_client()