from dao.factory import *
from flask import send_file
from flask import jsonify
from models import Client, Equipment
from flask_restx import Resource
from flask_marshmallow import Marshmallow
from application import app, api
from dao import client_dao, equipment_dao
from flask_cors import CORS, cross_origin
import decimal
import os

ma = Marshmallow(app)


class ClientSchema(ma.Schema):
    class Meta:
        model = Client
        fields = ("name", "cpf", "email", "id", "telefone")


class EquipmentSchema(ma.Schema):
    class Meta:
        model = Equipment
        fields = ("brand", "defect_for_repair", "model",
                  "id", "cost_value", "pronto", "entregue", "data_entrada", "client_id")


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/api/client-findById')
class Client_find_by_id(Resource):
    # POST
    def post(self):
        data = api.payload
        client = client_dao.find_by_id(data["id"])
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)

    def get(self):
        data = api.payload
        client = client_dao.find_by_id(data["id"])
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/api/equipment-findByDataEntrada')
class Equipment_find_by_id_data_entrada(Resource):
    # POST
    def post(self):
        data = api.payload
        print(data["data_entrada"])
        equipment = equipment_dao.find_by_entrada(data["data_entrada"])
        equipment_schema = EquipmentSchema(many=True)
        output = equipment_schema.dump(equipment)
        return jsonify(output)


@cross_origin()
@api.response(200, "Success")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@api.route('/api/client-findAll')
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
        equipment = Equipment(pronto=data["pronto"], entregue=data["entregue"], autorizado=True, client_id=data["idClient"], brand=data["brand"],
                              defect_for_repair=data["defect_for_repair"], model=data["model"], cost_value=data["preco"])

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


@api.route('/api/equipment-update')
class Equipment_update(Resource):
    def post(self):
        print("testando")
        data = api.payload
        equipment = equipment_dao.find_by_id(data["id"])
        equipment.id = data["id"]
        equipment.brand = data["brand"]
        equipment.cost_value = data["cost_value"]
        equipment.defect_for_repair = data["defect_for_repair"]
        equipment.model = data["model"]
        equipment.serial = data["serial"]
        equipment.pronto = data["pronto"]
        equipment.entregue = data["entregue"]
        equipment = equipment_dao.update(equipment)
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
        client.email = data["email"]
        client_dao.update(client)
        client_schema = ClientSchema()
        output = client_schema.dump(client)
        return jsonify(output)


@app.route('/download')
def downloadFile():
    # For windows you need to use drive name [ex: F:/Example.pdf]
    path = '/Users/maiquelknechtel/eclipse-workspace/generatePDF_maven/pdf/dynamic1.pdf'
    return send_file(path, as_attachment=True)
