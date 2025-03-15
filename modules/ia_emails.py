import requests
import re
from database.db_manager import db

def buscar_emails(url):
    response = requests.get(url)
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(padrao, response.text)

    for email in emails:
        db.insert_data("emails", {"email": email, "origem": url})
        print(f"Email encontrado: {email}")

buscar_emails("https://exemplo.com")
