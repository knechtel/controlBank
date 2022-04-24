from dao.factory import *
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
from dao import client_dao, equipment_dao
ma = Marshmallow(app)


class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ("name", "cpf", "email", "id")


class EquipmentSchema(ma.Schema):
    class Meta:
        model = Equipment
        fields = ("brand", "defect_for_repair", "model", "id")


#################################


@api.route('/api/')
class GetAndPost(Resource):

    # GET ALL
    def get(self):
        client_schema = ClientSchema(many=True)
        output = client_schema.dump(client_dao.find_all())
        return jsonify(output)

    # POST
    def post(self):
        data = api.payload
        client = Client(cpf=data["cpf"],
                        name=data["name"], email=data["email"])

        equipment_dao.save(client)

        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@api.route('/api/equipment')
class GetAndPost(Resource):

    # GET ALL
    def get(self):
        jsonStr = equipment_dao.find_all()
        equipment_schema = EquipmentSchema(many=True)
        output = equipment_schema.dump(jsonStr)
        return jsonify(output)

    def post(self):
        data = api.payload
        equipment = Equipment(pronto=True, autorizado=True, brand=data["brand"],
                              defect_for_repair=data["defect_for_repair"], model=data["model"])

        equipment_dao.save(equipment)
        equipment_schema = EquipmentSchema()
        output = equipment_schema.dump(equipment)
        return jsonify(output)
#################################
