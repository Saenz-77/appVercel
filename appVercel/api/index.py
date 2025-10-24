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

    url = "https://graph.facebook.com/v17.0/126262110574812/messages"
    headers = {
        'Authorization': 'Bearer TU_TOKEN_AQUI',
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
