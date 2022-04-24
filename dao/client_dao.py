
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
