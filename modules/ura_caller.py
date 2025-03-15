import requests
from flask import Flask, request, Response

app = Flask(__name__)

# Configuração do URL da API e chave de API
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
API_KEY = "AIzaSyAuFi5KtPsMJI5IC8c5FjvYD5IbuBdwH_U"

def obter_resposta_ia(mensagem):
"""Consulta a IA da API do Gemini para obter a resposta."""
headers = {
"Authorization": f"Bearer {API_KEY}",
"Content-Type": "application/json"
}
payload = {
"input": {
"text": mensagem
}
}
response = requests.post(API_URL, headers=headers, json=payload)
if response.status_code == 200:
return response.json().get("result", {}).get("content", "Desculpe, não entendi a pergunta.")
else:
return "Houve um erro ao acessar a IA."

@app.route('/voice', methods=['POST'])
def voice_response():
"""Recebe a chamada, escuta e responde com a IA."""
response = Response(
"<?xml version='1.0' encoding='UTF-8'?><Response><Say>Olá! Como posso ajudar você hoje?</Say>"
"<Gather input='speech' action='/process-response' method='POST'>"
"<Say>Por favor, fale sua dúvida.</Say></Gather></Response>",
mimetype='text/xml'
)
return response

@app.route('/process-response', methods=['POST'])
def process_response():
"""Processa a resposta do usuário e retorna a resposta da IA."""
mensagem_usuario = request.form.get('SpeechResult')
resposta_ia = obter_resposta_ia(mensagem_usuario)

# Resposta da IA lida em voz alta
return Response(f"<Response><Say>{resposta_ia}</Say></Response>", mimetype='text/xml')

if __name__ == "__main__":
app.run(port=5000)  # Certifique-se de rodar isto no servidor apropriado