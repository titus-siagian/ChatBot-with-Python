from flask import Flask, render_template, request, jsonify
import openai
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

# Endpoint untuk chatbot
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User: {user_input}\nChatbot:",
            max_tokens=150,
            temperature=0.7,
        )
        chatbot_response = response.choices[0].text.strip()
        return jsonify({"response": chatbot_response})
    except Exception as e:
        return jsonify({"response": f"Terjadi kesalahan: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
