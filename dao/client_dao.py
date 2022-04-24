
import sqlalchemy
from models import Client
from . import factory


def find_all():
    sessionobj = factory.connect()
    clients = sessionobj.query(Client).all()
    return clients
