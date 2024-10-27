"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend. It also contains the API endpoint for handling the GROQ API requests."""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector
import sql
import groq_module
import os

config = {
        'user': 'root',
        'password': 'jaguarJosh-25',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'finances'
    }


app = Flask(__name__)
CORS(app, origins='*') 

@app.route("/", methods=['GET', 'POST'])
def home():
    groq_module.translate()
    path = os.path.join(os.getcwd(), 'oh-snap', 'index.html')

@app.route("/query", methods=['POST', 'GET'])
def main():
    data = request.get_json()
    print(f"""Received data: {data}""")
    response = groq_module.chat_bot(data['query'])
    return jsonify({'response': response})


@app.route('/add_money', methods=['GET', 'POST'])
def add_money():
    sql.add_money(connection=mysql.connector.connect(**config))
    return {'response': "Money Added"}


if __name__ == "__main__":
    app.run(debug=True)