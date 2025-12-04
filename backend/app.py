"""This is the main file for the backend. It is responsible for running the Flask server and serving the frontend. It also contains the API endpoint for handling the GROQ API requests."""
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, jsonify, send_file
# Minimal run: avoid flask_login dependency
from flask_cors import CORS
import groq_module, os
from sql import add_money, get_balance, translate_text, get_db_connection, ensure_finance_table, get_user_by_username, create_user
import users


app = Flask(__name__)
CORS(app, origins='*') 

@app.route("/", methods=['GET', 'POST'])
def home():
    path = os.path.join(os.getcwd(), 'oh-snap', 'index.html')
    if os.path.exists(path):
        return send_file(path)
    return jsonify({'response': 'Index not found'}), 404

@app.route('/add_money', methods=['POST'])
def add_money_route():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    amount = data.get('amount')
    try:
        amt = float(amount)
        if amt <= 0:
            return jsonify({'error': 'amount must be a positive number'}), 400
        return add_money(username, amt)
    except Exception:
        return jsonify({'error': 'invalid amount'}), 400

@app.route('/balance', methods=['GET'])
def balance_route():
    username = request.args.get('username')
    return get_balance(username)

@app.route('/translate', methods=['POST'])
def translate_route():
    data = request.get_json(silent=True) or {}
    text = data.get('text')
    target_language = data.get('target_language')
    return translate_text(text, target_language)

@app.route("/query", methods=['POST', 'GET'])
def main():
    data = request.get_json()
    print(f"""Received data: {data}""")
    response = groq_module.chat_bot(data['query'])
    return jsonify({'response': response}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        print(f"""Received data: {data}""")
        # Support both nested and flat payloads
        username = data.get('username') or (data.get('username') or {}).get('username')
        password = data.get('password') or (data.get('password') or {}).get('password')
        if not username or not password:
            return jsonify({'response': 'username and password required'}), 400

        # DB-only auth: fetch from finances table
        db_user = get_user_by_username(username)
        if db_user and db_user[2] == password:
            return jsonify({'response': "Logged In", 'user': {'id': db_user[0], 'username': db_user[1]}}), 200
        return jsonify({'response': 'Invalid credentials'}), 200
    return jsonify({'response': 'Login endpoint'}), 200
    

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    return jsonify({'response': 'Logged Out'}), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'response': 'Username and password required'}), 400
    # DB-only user creation
    created = create_user(username, password)
    if not created:
        return jsonify({'response': 'Database unavailable for registration'}), 500
    # Initialize balance to 0 in DB if available
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            ensure_finance_table(conn)
            # Already handled in create_user
            conn.commit()
    except Exception:
        pass
    return jsonify({'response': 'User Created'}), 200

@app.route('/send_money', methods=['POST'])
def send_money_route():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    amount = data.get('amount')
    try:
        amt = float(amount)
        if amt < 0:
            return jsonify({'error': 'amount must be positive'}), 400
        # Subtract by adding a negative amount
        return add_money(username, -amt)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Optionally ensure MySQL FINANCES table exists if DB is configured
    try:
        conn = get_db_connection()
        if conn:
            ensure_finance_table(conn)
    except Exception:
        pass
    app.run(debug=True)