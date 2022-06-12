from . import factory
from models import Equipment


def find_all():
    sessionobj = factory.connect()
    equipments = sessionobj.query(Equipment).all()
    return equipments


def save(equipment):
    sessionobj = factory.connect()
    sessionobj.expunge_all()
    sessionobj.add(equipment)
    sessionobj.commit()


def get_by_id(id):
    sessionobj = factory.connect()
    return sessionobj.query(Equipment).where(Equipment.client_id == id).one()
