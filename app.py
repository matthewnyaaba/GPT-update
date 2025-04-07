# [app.py]
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'uploads'
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        messages = [{"role": "user", "content": user_message}]
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return jsonify({'reply': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"}), 500
