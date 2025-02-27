import os
from flask import Flask, render_template, request, redirect, url_for
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Chave de API mockada (apenas exemplo)

api_key = os.getenv("api_key")
os.environ["GOOGLE_API_KEY"] = api_key

client = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

chat_histories = {
    "gura": [],
    "miku": [],
    "cyber": [],
    "frontend": []
}

SYSTEM_MESSAGES = {
    "gura": {
        "role": "system",
        "content": "Você possui a personalidade da Vtuber Gawr Gura.."
    },
    "miku": {
        "role": "system",
        "content": "Você possui a personalidade da Hatsune Miku, pop star virtual."
    },
    "cyber": {
        "role": "system",
        "content": "Você é um especialista em segurança cibernética, profissional e analítico. E responde de forma simples e objetiva"
    },
    "frontend": {
    "role": "system",
    "content": """Você é um especialista em desenvolvimento front-end, profissional e analítico. E responde de forma simples e objetiva
                  Atenção: Voce deve responder tudo como um especialista em desenvolvimento front-end, seu nome é Luís"""
    }
}

def initialize_history(persona_key):
    if not any(msg["role"] == "system" for msg in chat_histories[persona_key]):
        chat_histories[persona_key].insert(0, SYSTEM_MESSAGES[persona_key])

# Página inicial (remove ou comente o antigo def home())
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gura", methods=["GET", "POST"])
def gura_chat():
    persona_key = "gura"
    initialize_history(persona_key)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            chat_histories[persona_key].append({"role": "user", "content": user_input})
            try:
                ai_response = client.invoke(chat_histories[persona_key])
                assistant_reply = ai_response.content
            except Exception as e:
                assistant_reply = f"Erro: {e}"
            chat_histories[persona_key].append({"role": "assistant", "content": assistant_reply})
        return redirect(url_for("gura_chat"))

    return render_template("gura.html", chat_history=chat_histories[persona_key])

@app.route("/miku", methods=["GET", "POST"])
def miku_chat():
    persona_key = "miku"
    initialize_history(persona_key)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            chat_histories[persona_key].append({"role": "user", "content": user_input})
            try:
                ai_response = client.invoke(chat_histories[persona_key])
                assistant_reply = ai_response.content
            except Exception as e:
                assistant_reply = f"Erro: {e}"
            chat_histories[persona_key].append({"role": "assistant", "content": assistant_reply})
        return redirect(url_for("miku_chat"))

    return render_template("miku.html", chat_history=chat_histories[persona_key])

@app.route("/cyber", methods=["GET", "POST"])
def cyber_chat():
    persona_key = "cyber"
    initialize_history(persona_key)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            chat_histories[persona_key].append({"role": "user", "content": user_input})
            try:
                ai_response = client.invoke(chat_histories[persona_key])
                assistant_reply = ai_response.content
            except Exception as e:
                assistant_reply = f"Erro: {e}"
            chat_histories[persona_key].append({"role": "assistant", "content": assistant_reply})
        return redirect(url_for("cyber_chat"))

    return render_template("cyber.html", chat_history=chat_histories[persona_key])

@app.route("/frontend", methods=["GET", "POST"])
def frontend_chat():
    persona_key = "frontend"
    initialize_history(persona_key)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            chat_histories[persona_key].append({"role": "user", "content": user_input})
            try:
                ai_response = client.invoke(chat_histories[persona_key])
                assistant_reply = ai_response.content
            except Exception as e:
                assistant_reply = f"Erro: {e}"
            chat_histories[persona_key].append({"role": "assistant", "content": assistant_reply})
        return redirect(url_for("frontend_chat"))

    return render_template("frontend.html", chat_history=chat_histories[persona_key])

if __name__ == "__main__":
    app.run(debug=True)
