from . import factory
from models import Equipment
from datetime import date

def find_all():
    sessionobj = factory.connect()
    equipments = sessionobj.query(Equipment).all()
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
    return sessionobj.query(Equipment).where(Equipment.client_id == id).one()
