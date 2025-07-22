# API de Portafolio de Proyectos

## Descripción

API RESTful desarrollada con FastAPI que proporciona acceso a una colección de proyectos de desarrollo de software. La API permite consultar proyectos, filtrarlos por nombre y acceder a sus detalles técnicos, incluyendo lenguajes de programación utilizados, descripciones y enlaces relevantes.

## Características Principales

- **Consulta de Proyectos**: Obtén una lista completa de todos los proyectos disponibles.
- **Búsqueda por Nombre**: Encuentra proyectos específicos por su nombre de repositorio.
- **Estructura de Datos Estándar**: Respuestas consistentes con información detallada de cada proyecto.
- **CORS Habilitado**: Fácil integración con aplicaciones web frontend.
- **Documentación Interactiva**: Documentación automática disponible en `/docs` (Swagger UI) y `/redoc`.

## Estructura del Proyecto

```
api/
├── main.py              # Punto de entrada de la aplicación
├── models/             
│   └── proyecto.py     # Modelos Pydantic para validación de datos
├── routers/
│   └── proyectos.py    # Rutas relacionadas con los proyectos
├── static/             # Archivos estáticos (ej. imágenes, screenshots)
└── utils/
    ├── loader.py       # Utilidades para cargar datos de proyectos
    └── screenshot.py   # Funcionalidad para capturas de pantalla (opcional)
```

## Modelo de Datos

Cada proyecto incluye la siguiente información:

- `titulo`: Título del proyecto
- `descripcion`: Descripción detallada
- `fecha`: Fecha de creación o última actualización (formato YYYY-MM-DD)
- `url`: Enlace al repositorio
- `lenguaje`: Lenguaje principal del proyecto
- `lenguajes_completos`: Desglose de todos los lenguajes utilizados con su cantidad de líneas
- `topics`: Etiquetas o categorías del proyecto
- `sitio_web`: URL del sitio web en vivo (si está disponible)
- `repositorio`: Nombre del repositorio (usado para búsquedas)

## Documentación de la API

### Obtener todos los proyectos

```http
GET /proyectos
```

**Respuesta Exitosa (200 OK)**
```json
[
  {
    "titulo": "Nombre del Proyecto",
    "descripcion": "Descripción del proyecto...",
    "fecha": "2023-01-01",
    "url": "https://github.com/usuario/repositorio",
    "lenguaje": "Python",
    "lenguajes_completos": {
      "Python": 10000,
      "HTML": 500
    },
    "topics": ["web", "api"],
    "sitio_web": "https://ejemplo.com",
    "repositorio": "nombre-repositorio"
  }
]
```

### Obtener un proyecto por nombre de repositorio

```http
GET /proyectos/{nombre_repositorio}
```

**Parámetros de Ruta**
- `nombre_repositorio` (string, requerido): Nombre del repositorio a buscar (case-insensitive)

**Respuesta Exitosa (200 OK)**
```json
{
  "titulo": "Nombre del Proyecto",
  "descripcion": "Descripción detallada...",
  "fecha": "2023-01-01",
  "url": "https://github.com/usuario/repositorio",
  "lenguaje": "Python",
  "lenguajes_completos": {
    "Python": 10000,
    "HTML": 500
  },
  "topics": ["web", "api"],
  "sitio_web": "https://ejemplo.com",
  "repositorio": "nombre-repositorio"
}
```

**Error (404 Not Found)**
```json
{
  "detail": "Proyecto 'nombre-inexistente' no encontrado."
}
```

## Configuración

1. Clona el repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

La aplicación estará disponible en `http://localhost:8000`

## Uso con Frontend

La API está configurada con CORS para permitir peticiones desde cualquier origen. Puedes consumirla fácilmente desde cualquier aplicación frontend:

```javascript
// Ejemplo de consumo con fetch
const response = await fetch('https://tudominio.com/api/proyectos');
const proyectos = await response.json();
```

## Despliegue

La API puede ser desplegada en cualquier servicio compatible con aplicaciones FastAPI como:
- Vercel
- Heroku
- Google Cloud Run
- AWS Lambda con API Gateway

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para soporte o consultas, por favor contacta a [tu información de contacto].