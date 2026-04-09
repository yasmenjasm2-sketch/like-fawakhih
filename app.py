from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return "Server is running 🔥"

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data["msg"])
    return {"status": "sent"}

@app.route("/messages")
def get_messages():
    return jsonify(messages)