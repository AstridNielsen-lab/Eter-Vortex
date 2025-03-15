import googlesearch
from database.db_manager import db

def buscar_sites(termo):
    query = f'"{termo}" site:.com OR site:.br'
    resultados = googlesearch.search(query, num=10, stop=10, pause=2)

    for url in resultados:
        db.insert_data("websites", {"url": url, "pesquisa": termo})
        print(f"Site encontrado: {url}")

buscar_sites("robôs de automação")
