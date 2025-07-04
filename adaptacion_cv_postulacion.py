import os
from dotenv import load_dotenv
from github.github_api import GitHubAPI
from utils.utils import guardar_json_repositorios, formatear_proyecto, combinar_repos, agregar_proyecto_al_json
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
        
        for c in range(len(repositories)):
            print(f"{c}")
        
            proyectos_cv = [formatear_proyecto(r) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
            #print(proyectos_cv[c])

            proyectos_about = [github.obtener_about_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
            #print(proyectos_about[c])

            proyectos_lenguajes = [github.get_languages_for_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
            #print("Proyectos lenguajes: ", proyectos_lenguajes[c])

            proyectos_combinados = combinar_repos(proyectos_cv, proyectos_about, proyectos_lenguajes)
            print(proyectos_combinados[c])

            agregar_proyecto_al_json(proyectos_combinados[c], "./data/proyectos_pre.json")

        

        # generar_cv(proyectos_destacados=proyectos_combinados[:8])
        # # Save repositories to a JSON file for further processing
        # guardar_json_repositorios(repositories)

        # #------------------------------------------
        # print("\nGenerando datos para portafolio...")
        # get_data_for_portafolio.main()
        # print("\nDatos para portafolio generados correctamente")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()