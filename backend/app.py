"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend. It also contains the API endpoint for handling the GROQ API requests."""
from dotenv import load_dotenv
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(f"""Received data: {data}""")
        username = data['username']
        print(f"""Username: {username["username"]}""")
        password = data['password']
        print(f"""pw: {password["password"]}""")

        user = users.User.get_by_username(username["username"])
        print(f"""user: {user}""")
        if user and user[2] == password["password"]:
            # login_user(user)
            return {'response': "Logged In", 'user': user}
        else:
            return{'response':'Invalid credentials'}
    

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