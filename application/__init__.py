from flask import Flask
from flask_restx import Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

cors = CORS(app,resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'application/json'

from application import routes

