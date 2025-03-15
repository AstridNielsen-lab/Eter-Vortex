from database.db_manager import db

def verificar_lead(email):
    leads = db.fetch_data("emails")
    emails_cadastrados = [lead['email'] for lead in leads]

    if email in emails_cadastrados:
        print(f"Lead {email} já foi contatado.")
        return True
    else:
        print(f"Novo lead encontrado: {email}")
        return False

verificar_lead("contato@exemplo.com")
