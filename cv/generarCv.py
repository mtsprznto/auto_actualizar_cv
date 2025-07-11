

from cv.pdf import PDF
from utils.utils import extraer_lenguajes_unicos, agrupar_lenguajes_por_categoria

def generar_cv(proyectos_destacados: list, output_path: str="./data/CV_Matias_Perez_Nauto.pdf"):
    """Genera un CV en PDF con la información de contacto, educación, proyectos y tecnologías."""
    pdf = PDF()
    pdf.add_page()
    pdf.add_font("Roboto", "", "font/Roboto/static/Roboto-Regular.ttf", uni=True)

    
    pdf.set_font("Roboto", "", 10)
    pdf.cell(0,6,"Puerto Varas - Chile • linkedin.com/in/matiaspereznauto/ • +569 75475781 • matiaspereznauto@gmail.com", ln=True, align="C")

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
    
    pdf.texto_doble_alineado(
        izquierda="Desarrollador FullStack - Gestpass S.A",
        derecha="Puerto Varas, Chile"
    )
    pdf.paragraph("Desarrollé una aplicación de gestión de contraseñas siguiendo las mejores prácticas de seguridad y desarrollo, implementando el patrón MVC para una estructura modular y eficiente. La aplicación permite almacenar, gestionar y encriptar contraseñas de manera segura, además de generar claves robustas con caracteres especiales. Para su desarrollo, utilicé Next.js y React, junto con diversas bibliotecas especializadas en seguridad y criptografía, asegurando un sistema confiable y escalable. Este proyecto refleja mi experiencia en desarrollo web y optimización de código, priorizando seguridad y usabilidad.")
    pdf.texto_doble_alineado(
        izquierda="Desarrollador FullStack - Academ S.A",
        derecha="Puerto Varas, Chile"
    )
    pdf.paragraph("La plataforma está diseñada con una arquitectura modular, basada en Node.js, utilizando Next.js para el frontend y un backend optimizado con Prisma y PostgreSQL. Se ha integrado Stripe para la gestión de pagos y Clerk para la autenticación de usuarios.")
    pdf.ln(1)

    # Proyectos 
    pdf.section_title("Proyectos")
    #print(f"Proyectos destacados: {proyectos_destacados}")
    # pdf.multi_section(proyectos_destacados)
    for proyecto in proyectos_destacados:
        pdf.render_proyecto(proyecto)

    #------------------------------------------
    # Educación
    pdf.section_title("Educación")
    pdf.multi_section([
        "Programación y Análisis de Sistemas, AIEP, 2024 - Actual",
        "Técnico Administración de Empresas RRHH, Colegio Felmer Niklitschek, 2017"
    ])
    pdf.ln(1)



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

    # Salvar PDF
    pdf.output(output_path)
    print(f"✅ CV exportado exitosamente como {output_path}")