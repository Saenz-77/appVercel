from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🟢 Servidor Flask en Vercel activo."

@app.route("/api/notificar-asesor", methods=["POST"])
def notificar_asesor():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        number = data.get("number")
        text = data.get("text")

        if not number or not text:
            return jsonify({"error": "Missing 'number' or 'text'"}), 400

        # Prepara solicitud
        url = "https://graph.facebook.com/v17.0/126262110574812/messages"
        token = os.environ.get("WHATSAPP_TOKEN")

        if not token:
            return jsonify({"error": "Token no definido en entorno"}), 500

        headers = {
            "Authorization": f"Bearer {token}",
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
        print("📥 Respuesta WhatsApp:", response.status_code, response.text)

        try:
            return jsonify(response.json()), response.status_code
        except Exception:
            return jsonify({"error": "No se pudo parsear JSON de respuesta", "raw": response.text}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
