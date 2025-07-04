import os
from dotenv import load_dotenv
from github.github_api import GitHubAPI
from utils.utils import guardar_json_repositorios, formatear_proyecto, combinar_repos, agregar_proyecto_al_json
from cv.generarCv import generar_cv
from data.format_for_portolio import get_data_for_portafolio
from ia.preguntar import seleccionar_proyectos
from utils.procesar_repositorios import procesar_y_guardar_repositorios

import json




# Load environment variables from .env file
load_dotenv()

def main():
    try:

        print("Dejame los detalles de la propuesta laboral")
        propuesta = input("Propuesta laboral: ")



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
        
        
        #procesar_y_guardar_repositorios(repositories, github, username, "./data/proyectos_pre.json")
        # for c in range(len(repositories)):
        #     print(f"Proyecto {c}")
        
        #     proyectos_cv = [formatear_proyecto(r) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        #     #print(proyectos_cv[c])

        #     proyectos_about = [github.obtener_about_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        #     #print(proyectos_about[c])

        #     proyectos_lenguajes = [github.get_languages_for_repo(username, r.get("name")) for r in sorted(repositories, key=lambda x: x['updated_at'], reverse=True)]
        #     #print("Proyectos lenguajes: ", proyectos_lenguajes[c])

        #     proyectos_combinados = combinar_repos(proyectos_cv, proyectos_about, proyectos_lenguajes)
        #     print(proyectos_combinados[c])

        #     """
        #     Probar si es mejor mandarle cada proyecto en cada iteracion para que pueda razonar sobre el proyecto, y luego fuera del bucle, que me harme el json con los proyectos mas importartes para la postulacion
        #     """
            
        #     agregar_proyecto_al_json(proyectos_combinados[c], "./data/proyectos_pre.json")

        proyectos_combinados = json.load(open("./data/proyectos_pre.json", "r", encoding="utf-8"))
        print("🔍 Proyectos combinados cargados:", len(proyectos_combinados))

        proyectos_seleccionados = seleccionar_proyectos(proyectos_combinados, propuesta)
        with open("./data/proyectos_destacados.json", "w", encoding="utf-8") as f:
            json.dump(proyectos_seleccionados, f, ensure_ascii=False, indent=2)

        print(f"✅ Se guardaron {len(proyectos_seleccionados)} proyectos seleccionados para la propuesta laboral.")


        generar_cv(proyectos_destacados=proyectos_seleccionados)
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