# src/utils/screenshot.py
import os
import requests
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

BASE_URL = "https://shot.screenshotapi.net/screenshot"
STATIC_DIR = Path(__file__).resolve().parent.parent / "static" / "previews"

def obtener_screenshot(sitio_url: str, repositorio: str) -> str:
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    archivo = STATIC_DIR / f"{repositorio}.png"

    if archivo.exists():
        return str(archivo)

    token = os.getenv("SCREENSHOT_API_KEY")
    if not token:
        raise Exception("SCREENSHOT_API_KEY no configurado.")

    if not isinstance(sitio_url, str):
        sitio_url = str(sitio_url)

    params = {
        "token": token,
        "url": str(sitio_url),
        "output": "image",
        "file_type": "png",
        "viewport": "1440x1024",
        "full_page": "true"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error al generar screenshot")

    with open(archivo, "wb") as f:
        f.write(response.content)

    return str(archivo)