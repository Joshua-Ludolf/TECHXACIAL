from flask_login import UserMixin
import mysql.connector
import os, app, sql


cursor = sql.db_connection_1.cursor(dictionary=True)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_by_id(user_id):
        cursor.execute("SELECT * FROM users WHERE ID = %s", (user_id,))
        user = cursor.fetchone()
        if user:
            return User(id=user['ID'], username=user['USERNAME'], password=user['PASSWORD'])
        return None

    @staticmethod
    def get_by_username(username):
        cursor.execute("SELECT * FROM users WHERE USERNAME = %s", (username,))
        user = cursor.fetchone()
        if user:
            return User(id=user['ID'], username=user['USERNAME'], password=user['PASSWORD'])
        return None

    @staticmethod
    def create_user(username, password):
        cursor.execute("INSERT INTO users (USERNAME, PASSWORD) VALUES (%s, %s)", (username, password))
        sql.db_connection_1.commit()

