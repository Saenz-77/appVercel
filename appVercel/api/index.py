# api/index.py

from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🟢 Servidor Flask en Vercel activo."

@app.route("/notificar-asesor", methods=["POST"])
def notificar_asesor():
    data = request.get_json()
    number = data.get("number")
    text = data.get("text")

    url = "https://graph.facebook.com/v22.0/834560259747367/messages"
    headers = {
        "Authorization": f"Bearer {os.environ.get('WHATSAPP_TOKEN')}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": { "body": text }
    }

    print("📤 Enviando a WhatsApp:", payload)
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return jsonify(response.json())
