from flask import Flask
import os

app = Flask(__name__)

@app.route("/env-test")
def env_test():
    return os.getenv("STORAGE_CONNECTION_STRING", "NOT FOUND")

import FlaskTemplate.views
