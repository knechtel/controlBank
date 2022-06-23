
import sqlalchemy
from sqlalchemy import desc
from models import Client

from . import factory


def find_all():
    sessionobj = factory.connect()
    clients = sessionobj.query(Client).order_by(desc((Client.id))).all()
    return clients


def save(client):
    sessionobj = factory.connect()
    sessionobj.expunge_all()
    sessionobj.add(client)
    sessionobj.commit()


def find_by_id(id):
    sessionobj = factory.connect()
    client = sessionobj.query(Client).get(id)
    sessionobj.close()
    print(client)
    return client


def update(client):
    sessionobj = factory.connect()
    sessionobj.query(Client).filter(Client.id == client.id)\
        .update({'name': client.name,
                 'email': client.email,
                 'telefone': client.telefone,
                 'cpf': client.cpf})
    sessionobj.commit()
    sessionobj.close()
