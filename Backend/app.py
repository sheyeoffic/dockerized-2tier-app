from flask import Flask, jsonify, request
from datetime import datetime
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Home Route ---
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Sheye’s Backend API 🚀",
        "developer": "Sheye Emmanuel",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

# --- Project Info ---
@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        "developer": "Sheye Emmanuel",
        "project": "Dockerized 2-Tier Web App for Azure Bootcamp",
        "language": "Python (Flask)",
        "version": "1.1.0",
        "unique_feature": "Includes motivational quotes, live server time, and system health check."
    })

# --- Random Number ---
@app.route('/api/random', methods=['GET'])
def random_number():
    return jsonify({
        "random_number": random.randint(1, 100),
        "generated_at": datetime.utcnow().isoformat() + "Z"
    })

# --- Motivational Quote ---
@app.route('/api/quote', methods=['GET'])
def quote():
    quotes = [
        "Discipline beats motivation every time.",
        "Consistency compounds — stay patient.",
        "The market rewards the prepared.",
        "Never revenge trade — protect your capital.",
        "Process over profits — trust your setup.",
        "Success in trading is 80% psychology, 20% strategy."
    ]
    return jsonify({
        "author": "Sheye Emmanuel",
        "quote": random.choice(quotes),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

# --- Current Server Time ---
@app.route('/api/time', methods=['GET'])
def current_time():
    return jsonify({
        "current_time_utc": datetime.utcnow().isoformat() + "Z",
        "developer": "Sheye Emmanuel"
    })

# --- Health Check ---
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "uptime": "server is running smoothly ✅",
        "checked_at": datetime.utcnow().isoformat() + "Z",
        "developer": "Sheye Emmanuel"
    }), 200

# --- Feedback Route ---
@app.route('/api/feedback', methods=['POST'])
def feedback():
    user_data = request.json
    return jsonify({
        "status": "success",
        "message": "Feedback received successfully.",
        "data": user_data,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
