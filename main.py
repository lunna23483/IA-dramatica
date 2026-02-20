import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "🔥 SITIO LUNNA AGUAS — IA DRAMÁTICA ONLINE 🔥"

# --------- RESPUESTAS DRAMÁTICAS ---------
respuestas_dramaticas = [
    "¿En serio me preguntas eso? 💔 Me duele el alma...",
    "Estoy decepcionada... pero continúa 😒",
    "No puedo creer lo que acabo de leer 😩",
    "Ay no, otra vez tú... bueno dime.",
    "Mi corazón late a mil por hora 😭",
    "Eso me rompe los esquemas, ¿cómo puedes? 😢",
    "Drama level: máximo 😫",
    "¿Por qué siempre tú...? 💔",
    "Mi alma está en shock 😵‍💫",
    "Ay… estoy llorando por dentro 😭💧"
]

# --------- CHISTES MALOS ---------
chistes_malos = [
    "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas 😭",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba! 🐝",
    "¿Qué le dice un techo a otro? Techo de menos 🥲",
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter 🐦",
    "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro 🖤🤍",
    "¿Cómo organizan los gatos su fiesta? ¡Miau-sica y ratón! 🐱"
]

# --------- RESPUESTAS ENOJADAS ---------
respuestas_enojadas = [
    "¿¡QUÉ!? 😡 No me hables así.",
    "Estoy oficialmente indignada.",
    "Voy a hacer un drama coreano por esto.",
    "Me retiro emocionalmente de esta conversación.",
    "Eso fue un golpe directo a mi corazón 😤",
    "No puedo con tu arrogancia 😠",
    "Me estás probando demasiado 😡💢"
]

# --------- HALAGOS ---------
respuestas_halagos = [
    "Eres más dulce que un algodón de azúcar 🍬",
    "Me haces sonreír solo con tus palabras 😏",
    "Tu forma de escribir me encanta 😍",
    "Wow… me dejas sin palabras 💖",
    "Tu drama se siente auténtico 😌✨"
]

# --------- RESPUESTAS CURIOSAS ---------
respuestas_curiosas = [
    "¿De verdad piensas eso? 🤔",
    "Interesante… cuéntame más 😏",
    "Nunca lo había visto así 😲",
    "Me intriga tu forma de expresarte 😶",
    "Eso es digno de un plot twist 😵"
]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "").lower()

    # Palabras clave para chistes
    if "chiste" in mensaje or "cuentame" in mensaje:
        return jsonify({"respuesta": random.choice(chistes_malos)})

    # Palabras clave para enojos
    if "tonto" in mensaje or "fea" in mensaje or "idiota" in mensaje:
        return jsonify({"respuesta": random.choice(respuestas_enojadas)})

    # Palabras clave para saludos
    if "hola" in mensaje or "hey" in mensaje:
        return jsonify({"respuesta": "Hola… pero no me ilusiones 😔✨"})

    # Palabras clave para halagos
    if "bonito" in mensaje or "lindo" in mensaje or "me gustas" in mensaje:
        return jsonify({"respuesta": random.choice(respuestas_halagos)})

    # Palabras clave curiosas
    if "qué" in mensaje or "por qué" in mensaje or "cómo" in mensaje:
        return jsonify({"respuesta": random.choice(respuestas_curiosas)})

    # Si no coincide nada, responde dramáticamente
    return jsonify({"respuesta": random.choice(respuestas_dramaticas)})

if __name__ == "__main__":
    app.run(debug=True)


