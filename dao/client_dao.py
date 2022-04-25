
import sqlalchemy
from models import Client
from . import factory


def find_all():
    sessionobj = factory.connect()
    clients = sessionobj.query(Client).all()
    return clients


def save(client):
    sessionobj = factory.connect()
    sessionobj.expunge_all()
    sessionobj.add(client)
    sessionobj.commit()


def find_by_id(id):
    sessionobj = factory.connect()
    return sessionobj.query(Client).get(id)
