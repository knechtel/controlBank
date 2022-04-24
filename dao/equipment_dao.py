from . import factory
from models import Equipment


def find_all():
    sessionobj = factory.connect()
    equipments = sessionobj.query(Equipment).all()
    return equipments
