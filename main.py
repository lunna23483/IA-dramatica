import random
from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mensaje = data.get("mensaje", "").lower()

    if "chiste" in mensaje:
        return jsonify({"respuesta": random.choice(chistes_malos)})

    if "tonto" in mensaje or "fea" in mensaje:
        return jsonify({"respuesta": random.choice(respuestas_enojadas)})

    if "hola" in mensaje:
        return jsonify({"respuesta": "Hola… pero no me ilusiones 😔✨"})

    return jsonify({"respuesta": random.choice(respuestas_dramaticas)})

if __name__ == "__main__":
    app.run(debug=True)