from flask import Flask, render_template, request, jsonify
import mysql.connector
import os



db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_ACCOUNTS')
}

db_connection_1 = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_ACCOUNTS')
)

db_connection_2 = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_USERS')
)

def add_money(connection):
    try:
            data = {'ID_NUM':"6000",'NAME' : "Juian", 'BALANCE' : "10.0"}  # Ensure Flask processes JSON input
            if not data:
                return jsonify({"error": "Invalid data"}), 400
            cursor = connection.cursor()
            query = "INSERT INTO ACCOUNT (ID_NUM, NAME, BALANCE) VALUES (%s, %s, %s)"
            cursor.execute(query, (data['ID_NUM'], data['NAME'], data['BALANCE']))
            connection.commit()
            return jsonify({"message": "Money added successfully"}), 201
    except Exception as e:
            return jsonify({"error": str(e)}), 500
    
def auth():
      pass