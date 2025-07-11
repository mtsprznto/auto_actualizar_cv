

from cv.pdf import PDF
from utils.utils import extraer_lenguajes_unicos, agrupar_lenguajes_por_categoria

def generar_cv(proyectos_destacados: list, output_path: str="./data/CV_Matias_Perez_Nauto.pdf"):
    """Genera un CV en PDF con la información de contacto, educación, proyectos y tecnologías."""
    pdf = PDF()
    pdf.add_page()

    #------------------------------------------
    # Info Personal
    # pdf.section_title("Información de Contacto")
    # pdf.multi_section([
    #     "Puerto Varas - Chile",
    #     "matiaspereznauto@gmail.com",
    #     "+56 9 7547 5781",
    #     "GitHub: www.github.com/mtsprznto",
    #     "LinkedIn: www.linkedin.com/in/matiaspereznauto/"
    # ])
    pdf.set_font("Arial", "", 10)
    pdf.cell(0,10,"Puerto Varas - Chile • www.linkedin.com/in/matiaspereznauto/ • +569 75475781 • matiaspereznauto@gmail.com", ln=True, align="C")
    #--------------------
    # DESCRIPCION
    pdf.set_font("Arial", "H", 10)
    pdf.cell(0,10,"Desarrollador de software con experiencia en Python, JavaScript, Next.js, PHP , SQL. Apasionado por crear soluciones eficientes, seguras y optimizadas, con enfoque en interfaces y mejores prácticas. Busco aportar en entornos dinámicos e innovadores.", ln=True, align="R")

    #------------------------------------------
    # Experencia profesional
    pdf.section_title("Experencia profesional")
    pdf.set_font("Arial", "B", 10)
    page_width = pdf.w - 2 * pdf.l_margin  # ancho usable del documento

    right_text = "Puerto Varas, Chile"
    right_text_width = pdf.get_string_width(right_text)
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width - right_text_width, 6, "")  # espacio hasta el texto
    pdf.cell(right_text_width, 6, right_text, ln=0, align="R")

    # Texto alineado a la izquierda (en la misma línea)
    left_text = "Desarrollador FullStack - Gestpass S.A"
    pdf.set_xy(pdf.l_margin, pdf.get_y())  # volver al inicio horizontal
    pdf.cell(page_width, 6, left_text, ln=1, align="L")



    #------------------------------------------
    # Proyectos 
    pdf.section_title("Proyectos Destacados")
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

    #------------------------------------------
    # Habilidades Blandas y Disponibilidad
    pdf.section_title("Habilidades")
    pdf.multi_section([
        "Comunicación | Autoaprendizaje | Trabajo en equipo",
        "Proactividad | Manejo del estrés"
    ])

    #------------------------------------------
    pdf.section_title("Disponibilidad")
    pdf.paragraph("Disponible para trabajar presencialmente en Santiago o de forma híbrida. Con disposición para viajar según se requiera.")

    # Salvar PDF
    pdf.output(output_path)
    print(f"✅ CV exportado exitosamente como {output_path}")