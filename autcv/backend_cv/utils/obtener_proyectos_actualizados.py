from github.github_api import GitHubAPI
from utils.procesar_repositorios import procesar_repositorios
from utils.utils import limpiar_readme_markdown

github_service = GitHubAPI()

async def obtener_proyectos_actualizados(username: str) -> list[dict]:
    """
    Obtiene los proyectos actualizados de GitHub para un usuario específico.
    """
    repos = github_service.get_all_user_repositories(username)
    if not repos:
        return []
    proyectos = procesar_repositorios(repos, github_service, username)
    return proyectos

async def anadir_readme_proyectos_seleccionados(username: str, proyectos_seleccionados: list[dict]) -> list[dict]:

    proyectos_enriquecidos_con_readme = []

    for proyecto in proyectos_seleccionados:
        try:
            readme_raw = github_service.obtener_readme_raw(username, proyecto["repositorio"])
            readme_limpio = limpiar_readme_markdown(readme_raw)
            proyecto["readme_raw"] = readme_limpio
            proyectos_enriquecidos_con_readme.append(proyecto)
        except Exception as e:
            print(f"⚠️ No se pudo obtener README de {proyecto['nombre']}: {str(e)}")
            # proyectos_enriquecidos.append(proyecto)  # Lo agregas igual, sin README
    
    return proyectos_enriquecidos_con_readme


