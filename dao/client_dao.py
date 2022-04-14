
import sqlalchemy
from models import *
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
Session = sessionmaker(bind=engine)
sessionobj = Session()


def find_all():
    return NULL
