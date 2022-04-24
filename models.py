# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from json import JSONEncoder

db = SQLAlchemy()


class AuthUserGroup(db.Model):
    __tablename__ = 'auth_user_group'

    auth_user_group_id = db.Column(db.BigInteger, primary_key=True)
    auth_group = db.Column(db.String(255))
    username = db.Column(db.String(255))


class  Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(255))
    email = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Equipment(db.Model):
    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(255))
    cost_value = db.Column(db.Float(asdecimal=True))
    defect_for_repair = db.Column(db.String(255))
    model = db.Column(db.String(255))
    serial = db.Column(db.String(255))
    client_id = db.Column(db.ForeignKey('client.id'), index=True)
    autorizado = db.Column(db.Boolean, nullable=True)
    pronto = db.Column(db.Boolean, nullable=False)
    data_entrega = db.Column(db.DateTime)
    data_entrada = db.Column(db.DateTime)

    client = db.relationship(
        'Client', primaryjoin='Equipment.client_id == Client.id', backref='equipments')


class Guest(db.Model):
    __tablename__ = 'guest'

    guest_id = db.Column(db.BigInteger, primary_key=True)
    address = db.Column(db.String(255))
    country = db.Column(db.String(255))
    email_address = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    state = db.Column(db.String(255))


t_hibernate_sequence = db.Table(
    'hibernate_sequence',
    db.Column('next_val', db.BigInteger)
)


class O(db.Model):
    __tablename__ = 'os'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.ForeignKey('client.id'), index=True)
    equipment_id = db.Column(db.ForeignKey('equipment.id'), index=True)

    client = db.relationship(
        'Client', primaryjoin='O.client_id == Client.id', backref='oes')
    equipment = db.relationship(
        'Equipment', primaryjoin='O.equipment_id == Equipment.id', backref='oes')


t_perfis = db.Table(
    'perfis',
    db.Column('user_id', db.ForeignKey('user.id'), nullable=False, index=True),
    db.Column('perfis', db.Integer)
)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    login = db.Column(db.String(255))
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))

# subclass JSONEncoder


class ClientEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
