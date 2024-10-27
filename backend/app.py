"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend."""
import g
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins during development

@app.route("/")
def main():
    return jsonify()

@app.route("/api/data", methods=['POST'])
def handle_data():
    data = request.get_json()
    response = g.groq(data['input'])
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run()