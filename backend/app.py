"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend. It also contains the API endpoint for handling the GROQ API requests."""
import g
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*') 

@app.route("/query", methods=['POST', 'GET'])
def main():
    data = request.get_json()
    print(f"""Received data: {data}""")
    response = g.groq(data['query'])
    return jsonify({'response': response})


@app.route("/education", methods=['GET', 'POST'])
def handle_data():
    data = request.get_json()
    response = g.groq(data['input'])
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)