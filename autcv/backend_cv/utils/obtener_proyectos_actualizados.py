from github.github_api import GitHubAPI
from utils.procesar_repositorios import procesar_repositorios

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