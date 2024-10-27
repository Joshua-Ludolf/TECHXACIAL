from dotenv import load_dotenv
import json
from flask_login import UserMixin
import mysql.connector
import os, app, sql

load_dotenv()
db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

cursor = db.cursor()

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        cursor.execute("SELECT * FROM USERS WHERE ID = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            return User(id=user['ID'], username=user['USERNAME'], password=user['PASSWORD'])
        return None

    @staticmethod
    def get_by_username(username):
        cursor.execute("SELECT * FROM FINANCES WHERE USERs = %s", (username,))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return 0

    @staticmethod
    def create_user(username, password):
        cursor.execute("INSERT INTO users (USERS, PASSWORD) VALUES (%s, %s)", (username, password))
        sql.db_connection_1.commit()

