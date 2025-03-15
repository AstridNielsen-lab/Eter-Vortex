import schedule
import time
import threading
from modules import ia_whatsapp, ia_emails, ia_websites, ia_palavraschave

def executar_tarefas():
    threads = []

    threads.append(threading.Thread(target=ia_whatsapp.buscar_numeros_whatsapp, args=("https://exemplo.com",)))
    threads.append(threading.Thread(target=ia_emails.buscar_emails, args=("https://exemplo.com",)))
    threads.append(threading.Thread(target=ia_websites.buscar_sites, args=("robôs de automação",)))
    threads.append(threading.Thread(target=ia_palavraschave.buscar_palavras_chave, args=("comprar robôs",)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# Agendamento das execuções
schedule.every(2).hours.do(executar_tarefas)  # Executa a cada 2 horas
schedule.every().day.at("08:00").do(executar_tarefas)  # Executa todos os dias às 08h

def iniciar_agendador():
    while True:
        schedule.run_pending()
        time.sleep(60)  # Aguarda 1 minuto entre execuções

if __name__ == "__main__":
    iniciar_agendador()
