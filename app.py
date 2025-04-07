import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        file = request.json.get("file", None)
        audio = request.json.get("audio", None)

        messages = [{"role": "user", "content": user_message}]

        if file:
            # Future: handle uploaded file content (text, PDF, etc.)
            messages.append({"role": "user", "content": f"[File uploaded: {file}]"})
        
        if audio:
            messages.append({"role": "user", "content": f"[Audio received: {audio}]"})
        
        # Multimodal (if desired): you can add vision/audio here when supported in interface
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

# ⬇️ Optional endpoint for file uploads in future
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    filename = file.filename

    # Save if needed or process here
    return jsonify({"status": f"File '{filename}' received successfully!"})

if __name__ == "__main__":
    # Bind to 0.0.0.0 for Render deployment
    app.run(host="0.0.0.0", port=5000, debug=True)
