
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



# def extraer_lenguajes_unicos(proyectos: list) -> list:
#     lenguajes = set()
#     for bloque in proyectos:
#         linea_1 = bloque.split("\n")[0]
#         if "(" in linea_1 and ")" in linea_1:
#             lang = linea_1.split("(")[-1].split(")")[0].strip()
#             if lang:
#                 lenguajes.add(lang)
#     return sorted(lenguajes)

def extraer_lenguajes_unicos(proyectos: list) -> list:
    lenguajes = {p.get("lenguaje", "").strip() for p in proyectos if p.get("lenguaje")}
    return sorted(lenguajes)




def combinar_repos(cv_blocks: list, about_data: list) -> list:
    combinados = []
    for cv_entry, about in zip(cv_blocks, about_data):
        bloques = cv_entry.strip().split("\n")
        if len(bloques) >= 4:
            combinados.append({
                "titulo": bloques[0],
                "descripcion": bloques[1],
                "fecha": bloques[2],
                "url": bloques[3],
                "lenguaje": about.get("lenguaje"),
                "topics": about.get("topics", []),
                "sitio_web": about.get("sitio_web"),
                "repositorio": about.get("nombre")
            })
    return combinados