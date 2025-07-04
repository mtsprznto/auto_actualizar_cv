from utils.utils import formatear_proyecto, combinar_repos, agregar_proyecto_al_json

def procesar_y_guardar_repositorios(repositories: list, github, username: str, ruta_salida: str) -> None:
    """
    Formatea, complementa y guarda la información de los repositorios en un JSON.
    """
    if not repositories:
        print("❌ No hay repositorios para procesar.")
        return

    print(f"\nFound {len(repositories)} repositories:")
    print("-" * 80)

    # Ordenar repos por actualización
    sorted_repos = sorted(repositories, key=lambda x: x['updated_at'], reverse=True)

    # Preparar datos para todos los proyectos
    proyectos_cv = [formatear_proyecto(r) for r in sorted_repos]
    proyectos_about = [github.obtener_about_repo(username, r.get("name")) for r in sorted_repos]
    proyectos_lenguajes = [github.get_languages_for_repo(username, r.get("name")) for r in sorted_repos]

    proyectos_combinados = combinar_repos(proyectos_cv, proyectos_about, proyectos_lenguajes)

    # Iterar y guardar cada uno
    for idx, proyecto in enumerate(proyectos_combinados):
        print(f"Proyecto {idx}: {proyecto['repositorio']}")
        agregar_proyecto_al_json(proyecto, ruta_salida)