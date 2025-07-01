

from cv.pdf import PDF
from utils.utils import extraer_lenguajes_unicos, agrupar_lenguajes_por_categoria

def generar_cv(proyectos_destacados: list):
    """Genera un CV en PDF con la información de contacto, educación, proyectos y tecnologías."""
    pdf = PDF()
    pdf.add_page()

    #------------------------------------------
    # Info Personal
    pdf.section_title("Información de Contacto")
    pdf.multi_section([
        "Puerto Varas - Chile",
        "matiaspereznauto@gmail.com",
        "+56 9 7547 5781",
        "GitHub: www.github.com/mtsprznto",
        "LinkedIn: www.linkedin.com/in/matiaspereznauto/"
    ])

    #------------------------------------------
    # Educación
    pdf.section_title("Educación")
    pdf.multi_section([
        "Programación y Análisis de Sistemas, AIEP, 2024 - Actual",
        "Técnico Administración de Empresas RRHH, Colegio Felmer Niklitschek, 2017"
    ])

    #------------------------------------------
    # Proyectos
    pdf.section_title("Proyectos Destacados")
    print(f"Proyectos destacados: {proyectos_destacados}")
    # pdf.multi_section(proyectos_destacados)
    for proyecto in proyectos_destacados:
        pdf.render_proyecto(proyecto)

    #------------------------------------------
    # Tecnologías y Conocimientos
    pdf.section_title("Tecnologías")

    langs = extraer_lenguajes_unicos(proyectos_destacados)
    #print("Lenguajes únicos detectados:", langs)
    grupos = agrupar_lenguajes_por_categoria(langs)
    print("Grupos de lenguajes:", grupos)

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
    pdf.output("./data/CV_Matias_Perez_Nauto.pdf")
    print("✅ CV exportado exitosamente como 'CV_Matias_Perez_Nauto.pdf'")