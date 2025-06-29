
from pdf import PDF

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
pdf.multi_section([
    "Academ – Plataforma educativa full stack. [academ-prod.vercel.app]",
    "Gestpass – Gestor de contraseñas con cifrado. [gestpass.vercel.app]",
    "CabañasPv – Web de arriendo de propiedades. [cabanaspv.vercel.app]",
    "Ecommerce-Coffe – Tienda online simulada (Front y Back). [coffedream.vercel.app]",
    "Portafolio Minimalista y otros landings desarrollados con React, Next.js y Tailwind CSS."
])

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