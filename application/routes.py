from dao.factory import *

from flask import jsonify
from models import Client, Equipment
from flask_restx import Resource
from flask_marshmallow import Marshmallow
from application import app, api
from dao import client_dao, equipment_dao
from flask_cors import CORS, cross_origin

ma = Marshmallow(app)


class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ("name", "cpf", "email", "id", "telefone")


class EquipmentSchema(ma.Schema):
    class Meta:
        model = Equipment
        fields = ("brand", "defect_for_repair", "model", "id", "cost_value")


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/client-findById')
class Client_find_by_id(Resource):
    # POST
    def post(self):
        data = api.payload
        client = client_dao.find_by_id(data["id"])
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/client-findAll')
class Client_get_post(Resource):

    # GET ALL
    def get(self):
        client_schema = ClientSchema(many=True)
        output = client_schema.dump(client_dao.find_all())
        return jsonify(output)

    # POST
    def post(self):
        data = api.payload
        client = Client(cpf=data["cpf"],
                        name=data["name"], email=data["email"], telefone=data["telefone"])

        client_dao.save(client)

        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/api/client')
class Client_get_post(Resource):

    # POST
    def post(self):
        data = api.payload
        client = Client(cpf=data["cpf"],
                        name=data["name"], email=data["email"], telefone=data["telefone"])

        client_dao.save(client)

        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)

@api.route('/api/equipment')
class Equipment_get_post(Resource):

    # GET ALL
    def get(self):
        jsonStr = equipment_dao.find_all()
        equipment_schema = EquipmentSchema(many=True)
        output = equipment_schema.dump(jsonStr)
        return jsonify(output)

    def post(self):
        data = api.payload
        equipment = Equipment(pronto=True, autorizado=True, client_id=data["idClient"], brand=data["brand"],
                              defect_for_repair=data["defect_for_repair"], model=data["model"])

        equipment_dao.save(equipment)
        equipment_schema = EquipmentSchema()
        output = equipment_schema.dump(equipment)
        return jsonify(output)


@api.route('/api/equipmentByIdClient')
class Equipment_by_id(Resource):
    def post(self):
        print("testando")
        data = api.payload
        equipment = equipment_dao.get_by_id_client(data["id"])
        equipment_schema = EquipmentSchema()
        output = equipment_schema.dump(equipment)
        return jsonify(output)


@api.route('/api/client-update')
class Equipment_by_id(Resource):
    def post(self):
        data = api.payload
        client = client_dao.find_by_id(data["id"])
        client.name = data["name"]
        client.telefone = data["telefone"]
        client.cpf = data["cpf"]
        client.cpf = data["email"]
        client_dao.update(client)
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)
