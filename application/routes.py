from flask import Flask, make_response, jsonify
from models import Client
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import json
from flask import jsonify
from flask_marshmallow import Marshmallow
from application import app

ma = Marshmallow(app)


@app.route("/")
def hello():
    return "hello 1!11"


class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ("name", "cpf", "email")


@app.route("/client/")
def client():
    engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
    Session = sessionmaker(bind=engine)
    sessionobj = Session()
    jsonStr = sessionobj.query(Client).all()
    client_schema = ClientSchema(many=True)
    sessionobj.commit()
    output = client_schema.dump(jsonStr)
    return jsonify(output)
