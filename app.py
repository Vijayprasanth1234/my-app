# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from ECS Fargate!"
#expose the Flask app to be run by the WSGI server