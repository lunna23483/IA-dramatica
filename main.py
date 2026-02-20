import random
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MEMORIA_FILE = "memoria.json"

# Función para cargar memoria
def cargar_memoria():
    try:
        with open(MEMORIA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Función para guardar memoria
def guardar_memoria(memoria):
    with open(MEMORIA_FILE, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

respuestas_dramaticas = [
    "¿En serio me preguntas eso? 💔 Me duele el alma...",
    "Estoy decepcionada... pero continúa 😒",
    "No puedo creer lo que acabo de leer 😩",
    "Ay no, otra vez tú... bueno dime."
]

chistes_malos = [
    "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas 😭",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba! 🐝",
    "¿Qué le dice un techo a otro? Techo de menos 🥲"
]

respuestas_enojadas = [
    "¿¡QUÉ!? 😡 No me hables así.",
    "Estoy oficialmente indignada.",
    "Voy a hacer un drama coreano por esto.",
    "Me retiro emocionalmente de esta conversación."
]

@app.route("/")
def home():
    return "🔥 SITIO LUNNA AGUAS — IA DRAMÁTICA ONLINE 🔥"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "").lower()

    memoria = cargar_memoria()

    # Guardar el mensaje del usuario
    memoria.append({"rol": "usuario", "mensaje": mensaje})

    # Lógica de respuesta
    if "chiste" in mensaje:
        respuesta = random.choice(chistes_malos)
    elif "tonto" in mensaje or "fea" in mensaje:
        respuesta = random.choice(respuestas_enojadas)
    elif "hola" in mensaje:
        respuesta = "Hola… pero no me ilusiones 😔✨"
    else:
        # Si la IA detecta que ya has hablado antes, responde recordando
        if memoria:
            ultimos = [m["mensaje"] for m in memoria if m["rol"] == "usuario"]
            if len(ultimos) > 1:
                respuesta = f"Recuerdo que dijiste: '{ultimos[-2]}', y ahora dices: '{mensaje}' 😏"
            else:
                respuesta = random.choice(respuestas_dramaticas)
        else:
            respuesta = random.choice(respuestas_dramaticas)

    # Guardar la respuesta de Lunna
    memoria.append({"rol": "lunna", "mensaje": respuesta})

    # Guardar memoria en JSON
    guardar_memoria(memoria)

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True)
