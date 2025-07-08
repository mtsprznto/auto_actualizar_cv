# Auto Actualizador de CV Profesional

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Una solución automatizada para mantener tu CV profesional siempre actualizado, extrayendo información directamente de tus repositorios de GitHub y generando un documento PDF listo para compartir.

## 🚀 Características Principales

- **Extracción Inteligente de Datos**: Obtiene metadatos detallados de tus repositorios de GitHub, incluyendo descripciones, lenguajes y estadísticas de participación.
- **Generación de PDF Profesional**: Crea documentos PDF bien estructurados utilizando ReportLab, con un diseño limpio y profesional.
- **Análisis de Habilidades**: Identifica y categoriza automáticamente las tecnologías que utilizas en tus proyectos.
- **Sistema de API Modular**: Arquitectura basada en módulos que permite fácil extensión y personalización.
- **Gestión de Dependencias**: Utiliza `requirements.txt` para un manejo claro de dependencias.
- **Seguridad**: Soporte para variables de entorno mediante `python-dotenv` para proteger información sensible.

## 🛠️ Tecnologías Clave

- **Lenguaje**: Python 3.8+
- **Generación de PDF**: ReportLab
- **API de GitHub**: Cliente personalizado con manejo de autenticación
- **Manejo de Dependencias**: pip
- **Formateo de Código**: Black
- **Variables de Entorno**: python-dotenv

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- Cuenta de GitHub con repositorios públicos/privados
- Token de acceso personal de GitHub (opcional pero recomendado)
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

## 🔧 Instalación Paso a Paso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/mtsprznto/auto_actualizar_cv.git
cd auto_actualizar_cv
```

### 2. Configuración del Entorno Virtual
Se recomienda utilizar un entorno virtual para gestionar las dependencias:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Linux/MacOS)
source venv/bin/activate

# Activar entorno (Windows)
.\venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración de GitHub API
1. Genera un token de acceso personal en GitHub:
   - Ve a [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
   - Genera un nuevo token con el alcance `public_repo`
   
2. Crea un archivo `.env` en la raíz del proyecto:
```env
GITHUB_TOKEN=tu_token_de_acceso_aquí
```

## 🚀 Guía de Uso

### Generación Básica del CV
```bash
python get_auto_actualizar_cv.py
```

### Opciones de Personalización
```bash
# Especificar usuario de GitHub diferente
python get_auto_actualizar_cv.py --usuario mi_usuario_github

# Especificar ruta de salida personalizada
python get_auto_actualizar_cv.py --output ruta/personalizada/mi_cv.pdf

# Incluir todos los repositorios (sin límite)
python get_auto_actualizar_cv.py --todos
```

### Estructura del Proyecto

```
┏━━ auto_actualizar_cv/
│   ┏━━ api/                   # API FastAPI para integración web
│   │   ├── __init__.py
│   │   ├── main.py              # Punto de entrada de la API
│   │   ├── models/              # Modelos de datos
│   │   ├── routers/             # Rutas de la API
│   │   └── utils/               # Utilidades de la API
│   ┏━━ cv/                    # Generación de documentos PDF
│   │   ├── __init__.py
│   │   ├── generarCv.py         # Lógica principal de generación
│   │   └── pdf.py               # Clase personalizada PDF
│   ┏━━ data/                  # Datos generados y recursos
│   │   ├── CV_*.pdf             # Archivos PDF generados
│   │   ├── proyectos_*.json     # Datos de repositorios
│   │   └── format_for_portfolio/ # Formato para portafolio web
│   ┏━━ github/                # Cliente de la API de GitHub
│   │   ├── __init__.py
│   │   └── github_api.py        # Cliente de la API
│   ┏━━ ia/                    # Integraciones con IA
│   │   ├── __init__.py
│   │   ├── connect.py          # Conexión con servicios de IA
│   │   └── preguntar.py        # Funcionalidad de preguntas
│   ┏━━ utils/                 # Utilidades generales
│   │   ├── __init__.py
│   │   └── utils.py            # Funciones auxiliares
│   ├── .env.example           # Ejemplo de configuración
│   ├── get_auto_actualizar_cv.py # Script principal
│   ├── get_all_repositorios.py  # Script alternativo
│   ├── README.md              # Documentación
│   └── requirements.txt       # Dependencias
└─━━ venv/                  # Entorno virtual (ignorado en git)
```

## 📝 Personalización Avanzada

### Modificar el Diseño del CV
El archivo principal de configuración se encuentra en `cv/pdf.py`. Puedes modificar:

- **Fuentes y colores**: Ajusta la tipografía y paleta de colores
- **Secciones personalizadas**: Añade o elimina secciones según tus necesidades
- **Diseño responsivo**: Ajusta los márgenes y espaciados

### Añadir Nuevas Fuentes
1. Coloca los archivos .ttf en la carpeta `data/fonts/`
2. Registra la fuente en `cv/pdf.py`:

```python
self.add_font('NombreFuente', '', 'ruta/a/la/fuente.ttf')
```

### Integración con Otras Plataformas
El proyecto puede extenderse para integrarse con:
- LinkedIn API para experiencia laboral
- Medium/Dev.to para publicaciones técnicas
- Plataformas de certificaciones (Coursera, Udemy, etc.)

## 🤝 Guía de Contribución

Apreciamos mucho las contribuciones de la comunidad. Antes de contribuir, por favor sigue estos pasos:

1. **Reporte de Errores y Sugerencias**
   - Revisa los [issues existentes](https://github.com/mtsprznto/auto_actualizar_cv/issues) para evitar duplicados
   - Proporciona información detallada sobre el error o la mejora propuesta
   - Incluye ejemplos de código, mensajes de error y capturas de pantalla cuando sea posible

2. **Proceso de Desarrollo**
   ```bash
   # 1. Haz un fork del repositorio
   # 2. Crea una rama para tu característica (git checkout -b feature/AmazingFeature)
   # 3. Haz commit de tus cambios (git commit -m 'Add some AmazingFeature')
   # 4. Haz push a la rama (git push origin feature/AmazingFeature)
   # 5. Abre un Pull Request
   ```

3. **Estándares de Código**
   - Sigue el estilo de código existente
   - Asegúrate de que tu código pase todas las pruebas
   - Actualiza la documentación según sea necesario
   - Mantén los commits atómicos y con mensajes descriptivos

## ⚠️ Solución de Problemas Comunes

### Error de Autenticación con GitHub
```
HTTP 403: API rate limit exceeded
```
**Solución:**
1. Crea un token de acceso personal en GitHub
2. Configóralo en tu archivo `.env` como `GITHUB_TOKEN=tu_token`

### Problemas con Dependencias
```
ModuleNotFoundError: No module named 'reportlab'
```
**Solución:**
```bash
pip install -r requirements.txt
```

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

```
MIT License

Copyright (c) 2024 Matías Pérez Nauto

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y de la documentación asociada (el "Software"), para tratar
el Software sin restricciones, incluyendo, sin limitación, los derechos de
uso, copia, modificación, fusión, publicación, distribución, sublicencia
y/o venta de copias del Software, y para permitir a las personas a las que se
les proporcione el Software a hacerlo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas
las copias o partes sustanciales del Software.
```

## 👥 Comunidad

Únete a nuestra comunidad para obtener ayuda y compartir ideas:
- [Issues de GitHub](https://github.com/mtsprznto/auto_actualizar_cv/issues)
- [Discusiones](https://github.com/mtsprznto/auto_actualizar_cv/discussions)

## ✨ Reconocimientos

- **Matías Pérez Nauto** - Desarrollador Principal
  - [GitHub](https://github.com/mtsprznto)
  - [LinkedIn](https://www.linkedin.com/in/matiaspereznauto/)
  - [Portafolio](https://mtsprznto.github.io)

### Bibliotecas y Herramientas Utilizadas
- [ReportLab](https://www.reportlab.com/) - Generación de PDF
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Manejo de variables de entorno
- [Requests](https://docs.python-requests.org/) - Peticiones HTTP
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web

---

<div align="center">
  💻 Hecho con ❤️ y Python · 👋 Contribuciones son bienvenidas!
</div>