# index.py
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "🟢 Servidor Flask en Vercel activo."

@app.route("/notificar-asesor", methods=["POST"])
def notificar_asesor():
    data = request.json
    number = data.get("number")
    text = data.get("text")

    url = "https://graph.facebook.com/v22.0/834560259747367/messages"
    headers = {
        'Authorization': 'Bearer EAFd59J08Mk8BPZCIXU90KLK43VFHZB0jn4oh6pZClCfRlXsWcRNCNZBJANWEpZAZBDhrvyo81FZAIkfkxvSZB5YQJNsp4kiZAlems9b6Iy6GUbZCLZAQN4SPuDFojr2JzS1mxNZCzSdYiYo8ci2YFzb5vZAMatOmmY3yXbhud3qWkpX2p57TpXNrJK6mMjFH3juVBWSVlnwZDZD',
        'Content-Type': 'application/json'
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {"body": text}
    }

    print("📤 Enviando a WhatsApp:", payload)
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return jsonify(response.json())
