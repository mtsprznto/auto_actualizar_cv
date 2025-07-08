# src/utils/screenshot.py
import os
import httpx
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

BASE_URL = "https://shot.screenshotapi.net/screenshot"
STATIC_DIR = Path(__file__).resolve().parent.parent / "static" / "previews"

async def obtener_screenshot(sitio_url: str, repositorio: str) -> str:
    """Genera un screenshot de un sitio web"""
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    archivo = STATIC_DIR / f"{repositorio}.png"

    if archivo.exists():
        return str(archivo)

    token = os.getenv("SCREENSHOT_API_KEY")
    if not token:
        raise Exception("SCREENSHOT_API_KEY no configurado.")

    if not isinstance(sitio_url, str):
        sitio_url = str(sitio_url)

    async with httpx.AsyncClient(timeout=httpx.Timeout(60.0)) as client:
        response = await client.get(BASE_URL, params={
            "token": token,
            "url": str(sitio_url),
            "output": "image",
            "file_type": "png",
            "viewport": "1440x1024",
            "full_page": "true"
        },
        follow_redirects=True,
        timeout=httpx.Timeout(60.0)
        )

        if response.status_code != 200:
            raise Exception(f"Error al generar screenshot: {response.status_code} - {response.text}")

        with open(archivo, "wb") as f:
            f.write(response.content)

    return str(archivo)