from flask import Flask
from routes.base import base
from routes.controllers import controllers

app = Flask(__name__)

app.register_blueprint(base)
app.register_blueprint(controllers)
