from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ta clé privée
API_KEY = "ENsqYh436zFj1vRdiM_-BeCT-jxNEPMlfa2aGTZamDg"

# Exemple de fonction pour répondre (ici, réponse fixe)
# On pourra plus tard la connecter à un vrai modèle IA
def get_answer(question):
    return f"Tu as demandé : {question}. Réponse : (ici, une IA pourrait répondre sans filtre)."

@app.route("/", methods=["GET"])
def home():
    return "✅ API en ligne et sécurisée avec clé privée"

@app.route("/v1/ask", methods=["POST"])
def ask():
    key = request.headers.get("Authorization")
    if key != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.get_json()
    question = data.get("question", "")
    answer = get_answer(question)
    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
