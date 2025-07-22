import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import json
from datetime import datetime
from pathlib import Path
from utils.utils import calcular_porcentaje_lenguajes

def exportar_proyectos_js(proyectos: list, salida="./data/format_for_portolio/data/projects.js"):
    salida_path = Path(salida)
    salida_path.parent.mkdir(parents=True, exist_ok=True)

    with open(salida_path, "w", encoding="utf-8") as f:
        f.write("export const PROJECTS = [\n")

        for proyecto in proyectos:
            title = proyecto["repositorio"].replace("-", " ").replace("_", " ").title()
            date = proyecto["fecha"]
            description = proyecto["descripcion"].replace('"', '\\"')
            topics = json.dumps(proyecto.get("topics") or [])

            lenguajes_completos= calcular_porcentaje_lenguajes(proyecto.get("lenguajes_completos", {}))
            #lenguajes_completos = proyecto.get("lenguajes_completos", {})
            sitio_web = proyecto.get("sitio_web", "")
            url = proyecto.get("url", "")
            technologies = json.dumps([*list(lenguajes_completos.keys())]) if lenguajes_completos else "[]"

            f.write("  {\n")
            f.write(f'    title: "{title}",\n')
            f.write(f'    image: null,\n')
            f.write(f'    date: "{date}",\n')
            f.write(f'    lenguajes_utilizados: {lenguajes_completos},\n')
            f.write(f'    topics: {topics},\n')
            f.write(f'    description: "{description}",\n')
            f.write(f'    technologies: {technologies},\n')
            f.write(f'    url_demo: "{sitio_web}",\n')
            f.write(f'    url_codigo: "{url}"\n')
            f.write("  },\n")

        f.write("];\n")

    print(f"✅ Archivo generado correctamente en {salida_path.absolute()}")


def main():
    proyectos_combinados = json.load(open("./data/proyectos_combinados.json", "r", encoding="utf-8"))
    exportar_proyectos_js(proyectos_combinados)


if __name__ == "__main__":
    main()
