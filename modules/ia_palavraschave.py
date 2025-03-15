from googlesearch import search
from database.db_manager import db

def buscar_palavras_chave(termo):
    resultados = list(search(termo, num=5, stop=5, pause=2))
    
    for resultado in resultados:
        db.insert_data("palavras_chave", {"termo": termo, "url": resultado})
        print(f"Palavra-chave '{termo}' encontrada em: {resultado}")

buscar_palavras_chave("comprar robôs de automação")
