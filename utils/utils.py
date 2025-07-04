
def limpiar_texto(texto: str) -> str:
    return (
        texto.replace("–", "-")
            .replace("“", '"').replace("”", '"')
            .replace("‘", "'").replace("’", "'")
            .encode("latin-1", "ignore")
            .decode("latin-1")
    )


# Save repositories to a JSON file for further processing
def guardar_json_repositorios(repositories: list, filename: str="./data/repositories.json"):
    import json
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(repositories, f, indent=2, ensure_ascii=False)
    print(f"\nRepository data saved to '{filename}'")


import json
from pathlib import Path

def agregar_proyecto_al_json(proyecto: dict, ruta: str = "./data/proyectos_destacados.json") -> None:
    """
    Agrega un nuevo proyecto al JSON si no existe ya por nombre de repositorio.
    Evita duplicados y crea el archivo si no existe. Valida estructura.
    """
    ruta_json = Path(ruta)
    ruta_json.parent.mkdir(parents=True, exist_ok=True)

    proyectos = []

    if ruta_json.exists():
        with open(ruta_json, "r", encoding="utf-8") as f:
            try:
                proyectos = json.load(f)
                # Validar que sea una lista de diccionarios
                if not isinstance(proyectos, list) or not all(isinstance(p, dict) for p in proyectos):
                    print("⚠️ El contenido del JSON no es una lista de proyectos válidos. Se reiniciará limpio.")
                    proyectos = []
            except json.JSONDecodeError:
                print("⚠️ El archivo estaba vacío o mal formado. Se iniciará limpio.")
                proyectos = []

    # Validar que el nuevo proyecto tiene clave "repositorio"
    if "repositorio" not in proyecto:
        print("❌ El proyecto no contiene la clave 'repositorio'. No se puede agregar.")
        return

    ya_existe = any(p.get("repositorio") == proyecto["repositorio"] for p in proyectos)

    if not ya_existe:
        proyectos.append(proyecto)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(proyectos, f, ensure_ascii=False, indent=2)
        print(f"✅ Proyecto '{proyecto['repositorio']}' agregado correctamente.")
    else:
        print(f"ℹ️ El proyecto '{proyecto['repositorio']}' ya existe en el archivo.")



def formatear_proyecto(repo: dict={}) -> str:
    nombre = repo.get("name", "Sin nombre")
    descripcion = repo.get("description", "Sin descripción")
    lenguaje = repo.get("language", "Desconocido")
    url = repo.get("html_url", "")
    actualizado = repo.get("updated_at", "").split("T")[0]


    nombre = str(nombre).upper()
    descripcion = str(descripcion)
    lenguaje = str(lenguaje)
    actualizado = str(actualizado)
    url = str(url)

    return (
        f"{nombre} ({lenguaje})\n"
        f"{descripcion}\n"
        f"{actualizado}\n"
        f"{url}\n\n"
    )





def extraer_lenguajes_unicos(proyectos: list) -> list:
    """Extrae todos los lenguajes únicos de los proyectos, combinando lenguajes_completos."""
    lenguajes = set()
    for proyecto in proyectos:
        lang_dict = proyecto.get("lenguajes_completos", {})
        if isinstance(lang_dict, dict):
            lenguajes.update(lang_dict.keys())
    return sorted(lenguajes)





def combinar_repos(cv_blocks: list, about_data: list, lenguajes_data: list) -> list:
    """Combina los datos de los proyectos con los datos de GitHub"""
    combinados = []
    for cv_entry, about, langs in zip(cv_blocks, about_data, lenguajes_data):
        bloques = cv_entry.strip().split("\n")
        if len(bloques) >= 4:
            combinados.append({
                "titulo": bloques[0],
                "descripcion": bloques[1],
                "fecha": bloques[2],
                "url": bloques[3],
                "lenguaje": about.get("lenguaje"),  # lenguaje principal
                "lenguajes_completos": langs,       # todos los lenguajes detectados por GitHub
                "topics": about.get("topics", []),
                "sitio_web": about.get("sitio_web"),
                "repositorio": about.get("nombre")
            })
    return combinados


def calcular_porcentaje_lenguajes(lenguajes: dict) -> dict:
    total = sum(lenguajes.values())
    return {
        lang: round((bytes_ * 100) / total, 2)
        for lang, bytes_ in lenguajes.items()
    }



def agrupar_lenguajes_por_categoria(lenguajes: list) -> dict:
    frontend = {"HTML", "CSS", "TypeScript", "JavaScript", "Blade", "Vue", "Svelte"}
    backend = {"PHP", "Java", "C#", "Go", "Ruby", "Rust", "Kotlin", "SQL"}
    scripting = {"Python", "Shell", "Bash", "PowerShell", "R", "Perl"}

    grupos = {"Frontend": [], "Backend": [], "Scripting": [], "Otros": []}

    for lang in lenguajes:
        if lang in frontend:
            grupos["Frontend"].append(lang)
        elif lang in backend:
            grupos["Backend"].append(lang)
        elif lang in scripting:
            grupos["Scripting"].append(lang)
        else:
            grupos["Otros"].append(lang)

    # Ordenar alfabéticamente
    return {k: sorted(set(v)) for k, v in grupos.items() if v}