import requests
import re
from database.db_manager import db

def buscar_numeros_whatsapp(url):
    response = requests.get(url)
    padrao = r'\+\d{1,3}\s?\(?\d{2,3}\)?\s?\d{4,5}-?\d{4}'
    numeros = re.findall(padrao, response.text)
    
    for numero in numeros:
        db.insert_data("whatsapp_contatos", {"numero": numero, "origem": url})
        print(f"Encontrado: {numero} - {url}")

buscar_numeros_whatsapp("https://exemplo.com")
