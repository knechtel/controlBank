from flask import Flask
from flask_restx import Api


app = Flask(__name__)
api = Api(app)

from application import routes

