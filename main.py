import threading
from modules import ia_whatsapp, ia_emails, ia_websites, ia_palavraschave

def iniciar_sistema():
    threads = []
    
    # Criando threads para cada módulo
    threads.append(threading.Thread(target=ia_whatsapp.buscar_numeros_whatsapp, args=("https://exemplo.com",)))
    threads.append(threading.Thread(target=ia_emails.buscar_emails, args=("https://exemplo.com",)))
    threads.append(threading.Thread(target=ia_websites.buscar_sites, args=("robôs de automação",)))
    threads.append(threading.Thread(target=ia_palavraschave.buscar_palavras_chave, args=("comprar robôs",)))
    
    # Iniciando as threads
    for thread in threads:
        thread.start()

    # Aguardando todas terminarem
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    iniciar_sistema()
