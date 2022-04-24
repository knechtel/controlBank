import sqlalchemy
from sqlalchemy.orm import sessionmaker


def connect():
    engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    sessionobj = Session()
    return sessionobj
