

from cv.pdf import PDF



def generar_cv(proyectos_destacados: list):
    """Genera un CV en PDF con la información de contacto, educación, proyectos y tecnologías."""
    pdf = PDF()
    pdf.add_page()

    # Info Personal
    pdf.section_title("Información de Contacto")
    pdf.multi_section([
        "Puerto Varas - Chile",
        "matiaspereznauto@gmail.com",
        "+56 9 7547 5781",
        "GitHub: github.com/mtsprznto",
        "LinkedIn: linkedin.com/in/matiaspereznauto/"
    ])

    # Educación
    pdf.section_title("Educación")
    pdf.multi_section([
        "Programación y Análisis de Sistemas, AIEP, 2024 - Actual",
        "Técnico Administración de Empresas RRHH, Colegio Felmer Niklitschek, 2017"
    ])


    # Proyectos
    pdf.section_title("Proyectos Destacados")
    pdf.multi_section(proyectos_destacados)


    # Tecnologías y Conocimientos
    pdf.section_title("Tecnologías")
    pdf.multi_section([
        "Lenguajes: Python, Java, C#, SQL, PHP",
        "Frameworks: React, Next.js, FastAPI, .NET, Flet",
        "Bases de Datos: MySQL, Oracle, SQL Server",
        "Herramientas: Visual Studio, VS Code",
        "Sistemas Operativos: Windows, Linux"
    ])

    # Habilidades Blandas y Disponibilidad
    pdf.section_title("Habilidades")
    pdf.multi_section([
        "Comunicación | Autoaprendizaje | Trabajo en equipo",
        "Proactividad | Manejo del estrés"
    ])

    pdf.section_title("Disponibilidad")
    pdf.paragraph("Disponible para trabajar presencialmente en Santiago o de forma híbrida. Con disposición para viajar según se requiera.")

    # Salvar PDF
    pdf.output("./data/CV_Matias_Perez_Nauto.pdf")
    print("✅ CV exportado exitosamente como 'CV_Matias_Perez_Nauto.pdf'")