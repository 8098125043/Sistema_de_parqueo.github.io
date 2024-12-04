from flask import Flask
from routes.short import short
from routes.base import base

app = Flask(__name__)

app.register_blueprint(short)
app.register_blueprint(base)
