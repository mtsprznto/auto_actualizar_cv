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
        
        
        procesar_y_guardar_repositorios(repositories, github, username, "./data/proyectos_pre.json")
        
        proyectos_combinados = json.load(open("./data/proyectos_pre.json", "r", encoding="utf-8"))
        print("🔍 Proyectos combinados cargados:", len(proyectos_combinados))

        proyectos_seleccionados = seleccionar_proyectos(proyectos_combinados, propuesta)
        with open("./data/proyectos_destacados.json", "w", encoding="utf-8") as f:
            json.dump(proyectos_seleccionados, f, ensure_ascii=False, indent=2)

        print(f"✅ Se guardaron {len(proyectos_seleccionados)} proyectos seleccionados para la propuesta laboral.")

        output_path = './data/Matias_Perez_Nauto_CV_select.pdf'
        generar_cv(proyectos_destacados=proyectos_seleccionados, output_path=output_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    while True:
        main()

        print("\n¿Querés generar otro CV con una propuesta diferente?")
        respuesta = input("Escribí 's' para sí o cualquier otra tecla para salir: ").strip().lower()

        if respuesta != "s":
            print("👋 Proceso finalizado. ¡Éxitos en tus postulaciones!")
            break
