import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    path = os.path.abspath()
    return path.jsonfiy()