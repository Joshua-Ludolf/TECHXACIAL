"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend. It also contains the API endpoint for handling the GROQ API requests."""
from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_cors import CORS
import mysql.connector
import sql, groq_module, os, users

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
    sql.add_money(connection=mysql.connector.connect(**sql.db_connection_1))
    return {'response': "Money Added"}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get_by_username(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            return{'response':'Invalid credentials'}
    return {'response': "Logged In"}

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.User.create_user(username, password)
        return redirect(url_for('login'))
    return {'response': "User Created"}


if __name__ == "__main__":
    app.run(debug=True)