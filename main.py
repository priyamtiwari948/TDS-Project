# main.py
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables from .env
load_dotenv()
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

app = Flask(__name__)

# Root route
@app.route("/")
def home():
    return "TDS Project API is running!"

# Test POST endpoint
@app.route("/api-endpoint", methods=["POST"])
def api_endpoint():
    data = request.get_json()
    
    # For testing, print received JSON
    print("Received data:", data)
    
    # Example response
    response = {
        "status": "success",
        "message": f"Hello {data.get('email', 'user')}! Your task '{data.get('task', '')}' was received."
    }
    return jsonify(response)

if __name__ == "__main__":
    # Debug mode ON for development
    app.run(debug=True)
