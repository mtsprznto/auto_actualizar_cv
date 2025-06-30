import os
from dotenv import load_dotenv
from github.github_api import GitHubAPI
from utils.utils import guardar_json_repositorios, formatear_proyecto, combinar_repos
from cv.generarCv import generar_cv

# Load environment variables from .env file
load_dotenv()

def main():
    try:
        # Initialize GitHub API client
        github = GitHubAPI()
        username = "mtsprznto"  # Your GitHub username
        
        print(f"Fetching all repositories for {username}...")
        repositories = github.get_all_user_repositories(username)
        
        

        if not repositories:
            print("No repositories found.")
            return
            
        print(f"\nFound {len(repositories)} repositories:")
        print("-" * 80)
        

        proyectos_cv = [formatear_proyecto(r) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        print(proyectos_cv[:8])
        proyectos_about = [github.obtener_about_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        print(proyectos_about[:8])

        proyectos_combinados = combinar_repos(proyectos_cv, proyectos_about)
        print(proyectos_combinados[:8])
        guardar_json_repositorios(proyectos_combinados[:8], "./data/proyectos_combinados.json")


        generar_cv(proyectos_destacados=proyectos_combinados[:8])
        # Save repositories to a JSON file for further processing
        guardar_json_repositorios(repositories)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()