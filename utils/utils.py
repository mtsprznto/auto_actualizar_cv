
def limpiar_texto(texto: str) -> str:
    return (
        texto.replace("–", "-")
            .replace("“", '"').replace("”", '"')
            .replace("‘", "'").replace("’", "'")
            .encode("latin-1", "ignore")
            .decode("latin-1")
    )


# Save repositories to a JSON file for further processing
def guardar_json_repositorios(repositories):
    import json
    with open('./data/repositories.json', 'w', encoding='utf-8') as f:
        json.dump(repositories, f, indent=2, ensure_ascii=False)
    print("\nRepository data saved to 'repositories.json'")


def formatear_proyecto(repo: dict={}) -> str:
    nombre = repo.get("name", "Sin nombre")
    descripcion = repo.get("description", "Sin descripción")
    lenguaje = repo.get("language", "Desconocido")
    url = repo.get("html_url", "")
    actualizado = repo.get("updated_at", "").split("T")[0]

    return (
        f"{nombre} ({lenguaje})\n"
        f"{descripcion}\n"
        f"📅 {actualizado}\n"
        f"🔗 {url}\n"
    )
