

from dotenv import load_dotenv
import os
from cv.pdf import PDF
from utils.utils import extraer_lenguajes_unicos, agrupar_lenguajes_por_categoria
from io import BytesIO
from pathlib import Path


import httpx

load_dotenv()



async def subir_cv_a_frontend(buffer: BytesIO, nombre_archivo: str) -> str:
    url_frontend_api = f"{os.getenv('URL_FRONTEND')}/api/upload/blob"  # Usa dominio final, no localhost
    async with httpx.AsyncClient() as client:
        files = {"file": (nombre_archivo, buffer, "application/pdf")}
        response = await client.post(url_frontend_api, files=files)
        if response.status_code == 200:
            print("✅ PDF subido al blob:", response.json()["url"])
            return response.json()["url"]
        else:
            print("❌ Error al subir PDF:", response.text)
            return None



async def generar_cv(proyectos_destacados: list,experiencias_cv:list , nombre_archivo: str):
    """Genera un CV en PDF con la información de contacto, educación, proyectos y tecnologías."""
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Helvetica", size=10)

    pdf.cell(0,6,"Puerto Varas - Chile - linkedin.com/in/matiaspereznauto/ - +569 75475781 - matiaspereznauto@gmail.com", ln=True, align="C")

    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    
    pdf.ln(1)
    #--------------------
    # DESCRIPCION
    pdf.ln(3)
    pdf.set_font("Arial", "I", 10)
    pdf.multi_cell(0, 6, "Desarrollador de software con experiencia en Python, JavaScript, Next.js, PHP , SQL. Apasionado por crear soluciones eficientes, seguras y optimizadas, con enfoque en interfaces y mejores prácticas. Busco aportar en entornos dinámicos e innovadores.", align="L")
    pdf.ln(3)
    #------------------------------------------
    # Experencia profesional
    pdf.section_title("Experiencia")
    for experiencia in experiencias_cv:
        pdf.texto_doble_alineado(
                izquierda=experiencia["titulo"],
                derecha="Puerto Varas, Chile"
            )
        pdf.paragraph(experiencia["experiencia_cv"])
        keywords = ", ".join(experiencia["keywords_detectadas"])
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_text_color(100, 100, 100)  # Gris suave
        pdf.multi_cell(0, 5, f"🔑 Tecnologías y conceptos clave: {keywords}", align="L")
        pdf.set_text_color(0, 0, 0)  # Restaurar color negro
        pdf.ln(2)

    # pdf.texto_doble_alineado(
    #     izquierda="Desarrollador FullStack - Gestpass S.A",
    #     derecha="Puerto Varas, Chile"
    # )
    # pdf.paragraph("Desarrollé una aplicación de gestión de contraseñas siguiendo las mejores prácticas de seguridad y desarrollo, implementando el patrón MVC para una estructura modular y eficiente. La aplicación permite almacenar, gestionar y encriptar contraseñas de manera segura, además de generar claves robustas con caracteres especiales. Para su desarrollo, utilicé Next.js y React, junto con diversas bibliotecas especializadas en seguridad y criptografía, asegurando un sistema confiable y escalable. Este proyecto refleja mi experiencia en desarrollo web y optimización de código, priorizando seguridad y usabilidad.")
    # pdf.texto_doble_alineado(
    #     izquierda="Desarrollador FullStack - Academ S.A",
    #     derecha="Puerto Varas, Chile"
    # )
    # pdf.paragraph("La plataforma está diseñada con una arquitectura modular, basada en Node.js, utilizando Next.js para el frontend y un backend optimizado con Prisma y PostgreSQL. Se ha integrado Stripe para la gestión de pagos y Clerk para la autenticación de usuarios.")
    pdf.ln(1)
    #---------------------------------------------------

    # Proyectos 
    pdf.section_title("Proyectos")
    #print(f"Proyectos destacados: {proyectos_destacados}")
    # pdf.multi_section(proyectos_destacados)
    for proyecto in proyectos_destacados:
        pdf.render_proyecto(proyecto)

    #------------------------------------------
    # EDUCACION
    pdf.section_title("Educación")
    pdf.texto_doble_alineado(
        izquierda="AIEP, 2024 - 2026",
        derecha="Puerto Varas, Chile"
    )
    pdf.paragraph("Programación y Análisis de Sistemas")
    pdf.ln(1)

    #------------------------------------------
    #------------------------------------------
    # Habilidades Blandas y Disponibilidad
    pdf.section_title("Habilidades")
    pdf.multi_section([
        "Comunicación | Autoaprendizaje | Trabajo en equipo | Proactividad | Manejo del estrés"
    ])
    pdf.ln(1)
    

    #------------------------------------------
    # Tecnologías y Conocimientos
    pdf.section_title("Tecnologías")

    langs = extraer_lenguajes_unicos(proyectos_destacados)
    #print("Lenguajes únicos detectados:", langs)
    grupos = agrupar_lenguajes_por_categoria(langs)
    #print("Grupos de lenguajes:", grupos)

    bloques = []
    if grupos.get("Frontend"):
        bloques.append(f"Frontend: {', '.join(grupos['Frontend'])}")
    if grupos.get("Backend"):
        bloques.append(f"Backend: {', '.join(grupos['Backend'])}")
    if grupos.get("Scripting"):
        bloques.append(f"Scripting: {', '.join(grupos['Scripting'])}")
    if grupos.get("Otros"):
        bloques.append(f"Otros: {', '.join(grupos['Otros'])}")

    bloques.extend([
        "Frameworks: React, Next.js, FastAPI, .NET, Flet",
        "Bases de Datos: MySQL, Oracle, SQL Server",
        "Herramientas: Visual Studio, VS Code",
        "Sistemas Operativos: Windows, Linux"
    ])

    pdf.multi_section(bloques)
    pdf.ln(1)
    

    #------------------------------------------
    pdf.section_title("Disponibilidad")
    pdf.paragraph("Disponible para trabajar presencialmente en Santiago o de forma híbrida. Con disposición para viajar según se requiera.")

    # PDF en memoria con BytesIO
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    buffer = BytesIO(pdf_bytes)
    buffer.seek(0)      # Posicionamos al inicio para lectura

    # Enviamos a frontend (Next.js)
    url_frontend_api = f"{os.getenv('URL_FRONTEND')}/api/upload/blob"  # Usa dominio final, no localhost
    async with httpx.AsyncClient() as client:
        files = {"file": (nombre_archivo, buffer, "application/pdf")}
        response = await client.post(url_frontend_api, files=files)
        if response.status_code == 200:
            print("✅ PDF subido al blob:", response.json()["url"])
            return response.json()["url"]
        else:
            print("❌ Error al subir PDF:", response.text)
            return None
