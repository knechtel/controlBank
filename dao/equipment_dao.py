from . import factory
from models import Equipment
from datetime import date
from sqlalchemy import func
from datetime import date


def find_all():
    sessionobj = factory.connect()
    equipments = sessionobj.query(Equipment).all()
    sessionobj.close()
    return equipments


def save(equipment):
    sessionobj = factory.connect()
    sessionobj.expunge_all()
    if(equipment.data_entrada == None):
        today = date.today()
        equipment.data_entrada = today
    sessionobj.add(equipment)
    sessionobj.commit()


def get_by_id_client(id):
    sessionobj = factory.connect()
    equipment = sessionobj.query(Equipment).where(
        Equipment.client_id == id).one()
    sessionobj.close()
    return equipment


def update(equipment):
    sessionobj = factory.connect()
    sessionobj.query(Equipment).filter(Equipment.id == equipment.id)\
        .update({'brand': equipment.brand,
                 'cost_value': equipment.cost_value,
                 'defect_for_repair': equipment.defect_for_repair,
                 'model': equipment.model,
                 'serial': equipment.serial,
                 'pronto': equipment.pronto,
                 'entregue': equipment.entregue})
    sessionobj.commit()
    sessionobj.close()


def find_by_id(id):
    sessionobj = factory.connect()
    equipment = sessionobj.query(Equipment).get(id)
    sessionobj.close()
    return equipment


def find_by_entrada(data_entrada):
    sessionobj = factory.connect()
    equipments = sessionobj.query(Equipment)\
        .filter(
        Equipment.data_entrada == date(int(data_entrada[6:10]), int(
            data_entrada[3:5]), int(data_entrada[0:2])))\
        .all()
    sessionobj.close()
    print(equipments)
    return equipments
