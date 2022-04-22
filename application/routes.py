import equipamento_controller
from flask import Flask, make_response, jsonify
from models import Client, Equipment
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import json
from flask import jsonify
from flask_restx import Resource
from flask_marshmallow import Marshmallow
from application import app, api

ma = Marshmallow(app)


@app.route("/")
def hello():
    return "hello 1!11"


class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ("name", "cpf", "email", "id")


class EquipmentSchema(ma.Schema):
    class Meta:
        model = Equipment
        fields = ("brand", "defect_for_repair", "model", "id")


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

#################################


@api.route('/api/')
class GetAndPost(Resource):

    # GET ALL
    def get(self):
        engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
        Session = sessionmaker(bind=engine)
        sessionobj = Session()
        jsonStr = sessionobj.query(Client).all()
        client_schema = ClientSchema(many=True)
        sessionobj.commit()
        output = client_schema.dump(jsonStr)
        return jsonify(output)
    #POST

    def post(self):
        data = api.payload
        client = Client(cpf=data["cpf"],
                        name=data["name"], email=data["email"])
        print("passei aqui...")
        engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
        Session = sessionmaker(bind=engine)
        sessionobj = Session()
        sessionobj.add(client)
        sessionobj.commit()
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@api.route('/api/equipment')
class GetAndPost(Resource):

    # GET ALL
    def get(self):
      engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
      Session = sessionmaker(bind=engine)
      sessionobj = Session()
      jsonStr = sessionobj.query(Equipment).all()
      equipment_schema = EquipmentSchema(many=True)
      sessionobj.commit()
      output = equipment_schema.dump(jsonStr)
      return jsonify(output)
#################################
