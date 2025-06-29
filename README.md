# Auto Actualizar CV

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una aplicación en Python que automatiza la actualización de tu CV con información de tus repositorios de GitHub.

## 🚀 Características

- Obtiene automáticamente información de tus repositorios de GitHub
- Genera un CV en formato PDF con un diseño limpio y profesional
- Incluye estadísticas de tus proyectos como estrellas, forks y lenguajes utilizados
- Fácil de personalizar según tus necesidades

## 📋 Requisitos

- Python 3.8 o superior
- Cuenta de GitHub
- Token de acceso personal de GitHub

## 🔧 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/auto_actualizar_cv.git
   cd auto_actualizar_cv
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: .\venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto con tu token de GitHub:
   ```
   API_KEY_GITHUB=tu_token_aqui
   ```

## 🚀 Uso

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```

2. El script generará un archivo JSON con la información de tus repositorios y actualizará automáticamente tu CV en formato PDF.

## 🏗️ Estructura del Proyecto

```
.
├── cv/                    # Módulo para la generación del CV
│   ├── pdf.py            # Clase personalizada para generar PDFs
│   └── generarCv.py      # Lógica para generar el CV
├── github/               # Módulo para interactuar con la API de GitHub
│   ├── github_api.py     # Cliente de la API de GitHub
│   └── __init__.py
├── data/                 # Datos generados
│   └── repositories.json # Información de repositorios guardada
├── utils/                # Utilidades
│   └── utils.py          # Funciones auxiliares
├── main.py               # Punto de entrada de la aplicación
└── README.md             # Este archivo
```

## 📝 Personalización

Puedes personalizar el diseño del CV editando la clase `PDF` en `cv/pdf.py`. Las secciones incluyen:

- Encabezado con nombre y título
- Títulos de sección
- Listas de elementos
- Párrafos de texto

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

## ✨ Créditos

- [Matías Pérez Nauto](https://github.com/mtsprznto) - Desarrollador

---

Hecho con ❤️ y Python