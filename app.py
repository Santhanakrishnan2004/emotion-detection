import os
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
# headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

API_URL = "https://router.huggingface.co/hf-inference/models/bhadresh-savani/distilbert-base-uncased-emotion"
headers = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
    "Content-Type": "application/json"
}


def analyze_emotion(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    if response.status_code == 200:
        return response.json()[0]
    else:
        return {"error": response.text}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['entry']
    result = analyze_emotion(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
