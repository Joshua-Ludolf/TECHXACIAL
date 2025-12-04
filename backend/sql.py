from flask import jsonify
import os
from dotenv import load_dotenv

try:
    import mysql.connector  # Optional: used only if available
except Exception:
    mysql_connector_available = False
else:
    mysql_connector_available = True

# In-memory balances store for dev without MySQL
_balances = {}

def _get_conn():
    """Return a live MySQL connection if available, else None."""
    if not mysql_connector_available:
        return None
    conn = get_db_connection()
    if conn:
        try:
            ensure_finance_table(conn)
        except Exception:
            pass
    return conn
def add_money(username: str, amount: float):
    try:
        if not username or amount is None:
            return jsonify({"error": "username and amount required"}), 400
        # Prefer DB when available
        conn = _get_conn()
        if conn:
            try:
                cursor = conn.cursor()
                # Upsert: add to existing balance or insert new row
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS `finances` (
                        `id` INT AUTO_INCREMENT PRIMARY KEY,
                        `username` VARCHAR(255) NOT NULL UNIQUE,
                        `password` VARCHAR(255) NOT NULL DEFAULT '',
                        `balance` DECIMAL(18,2) NOT NULL DEFAULT 0
                    )
                    """
                )
                cursor.execute(
                    """
                    INSERT INTO `finances` (username, balance)
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE balance = balance + VALUES(balance)
                    """,
                    (username, float(amount))
                )
                conn.commit()
                cursor.execute("SELECT balance FROM `finances` WHERE username = %s", (username,))
                row = cursor.fetchone()
                new_balance = float(row[0]) if row else 0.0
                return jsonify({"message": "Money added successfully", "username": username, "balance": new_balance}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        # Fallback: in-memory store
        current = float(_balances.get(username, 0.0))
        _balances[username] = current + float(amount)
        return jsonify({"message": "Money added successfully", "username": username, "balance": _balances[username]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_balance(username: str):
    try:
        if not username:
            return jsonify({"error": "username required"}), 400
        conn = _get_conn()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT balance FROM `finances` WHERE username = %s", (username,))
                row = cursor.fetchone()
                bal = float(row[0]) if row else 0.0
                return jsonify({"username": username, "balance": bal}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        # Fallback: in-memory
        bal = float(_balances.get(username, 0.0))
        return jsonify({"username": username, "balance": bal}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def translate_text(text: str, target_language: str):
    # Placeholder translation to keep dev environment DB-free and API-free
    if not text or not target_language:
        return jsonify({"error": "text and target_language required"}), 400
    return jsonify({
        "original": text,
        "target_language": target_language,
        "translatedText": f"[{target_language}] {text}"
    }), 200

# Optional MySQL helpers (safe to ignore if no DB configured)
def get_db_connection():
    """Connect to MySQL, ensuring target DB exists; return connection bound to it."""
    if not mysql_connector_available:
        return None
    load_dotenv()
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    db_name = (os.getenv('DB_NAME') or 'techxacial')
    # Create database if needed
    try:
        tmp = mysql.connector.connect(host=host, user=user, password=password)
        cur = tmp.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
        tmp.commit()
        cur.close(); tmp.close()
    except Exception:
        pass
    # Return connection to the database
    try:
        return mysql.connector.connect(host=host, user=user, password=password, database=db_name)
    except Exception:
        return None

def ensure_finance_table(connection):
    """Create `finances` table in the current database if missing.
    Columns: id, username (UNIQUE), password, balance.
    """
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        # Create table if missing
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS `finances` (
                `id` INT AUTO_INCREMENT PRIMARY KEY,
                `username` VARCHAR(255) NOT NULL UNIQUE,
                `password` VARCHAR(255) NOT NULL,
                `balance` DECIMAL(18,2) NOT NULL DEFAULT 0
            )
            """
        )
        # Ensure required columns exist in case of legacy schema
        try:
            cursor.execute("ALTER TABLE `finances` ADD COLUMN `password` VARCHAR(255) NOT NULL DEFAULT ''")
        except Exception:
            pass
        try:
            cursor.execute("ALTER TABLE `finances` ADD COLUMN `balance` DECIMAL(18,2) NOT NULL DEFAULT 0")
        except Exception:
            pass
        connection.commit()
        return True
    except Exception:
        return False

def get_user_by_username(username: str):
    """Return (id, username, password, balance) from finances if exists, else None."""
    conn = _get_conn()
    if not conn:
        # Fallback: in-memory store has no password; return None
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password, balance FROM `finances` WHERE username = %s", (username,))
        row = cursor.fetchone()
        return row if row else None
    except Exception:
        return None

def create_user(username: str, password: str):
    """Create a user in finances with 0 balance; upsert keeps balance at 0 and stores password."""
    conn = _get_conn()
    if not conn:
        # Fallback: no DB available; do nothing
        return False
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO `finances` (username, password, balance)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE password = VALUES(password), balance = COALESCE(balance, 0)
            """,
            (username, password, 0.0)
        )
        conn.commit()
        return True
    except Exception:
        return False
    