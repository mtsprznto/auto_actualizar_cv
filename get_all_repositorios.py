import os
from dotenv import load_dotenv
from github.github_api import GitHubAPI
from utils.utils import guardar_json_repositorios, formatear_proyecto, combinar_repos
from cv.generarCv import generar_cv
from data.format_for_portolio import get_data_for_portafolio




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
        proyectos_about = [github.obtener_about_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        proyectos_lenguajes = [github.get_languages_for_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]

        proyectos_combinados = combinar_repos(proyectos_cv, proyectos_about, proyectos_lenguajes)
        print("Proyectos combinados:", proyectos_combinados)
        proyectos_filtrados = [p for p in proyectos_combinados if p["repositorio"].lower() != "mtsprznto"]

        guardar_json_repositorios(proyectos_filtrados, "./data/proyectos_combinados_all.json")
        
        generar_cv(proyectos_destacados=proyectos_combinados, output_path='./data/CV_Matias_Perez_Nauto_all.pdf')
        # Save repositories to a JSON file for further processing
        guardar_json_repositorios(repositories, "./data/repositories_all.json")

        #------------------------------------------
        print("\nGenerando datos para portafolio...")
        get_data_for_portafolio.main()
        print("\nDatos para portafolio generados correctamente")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()