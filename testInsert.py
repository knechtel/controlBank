import sqlalchemy
from models import *
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql://root:123@localhost/loja')
Session = sessionmaker(bind=engine)
sessionobj = Session()


client = Client()
client.name = "Frederico"
client.cpf = "016.379.480-32"
client.email = "fredknechtel@gmail.com"

sessionobj.add(client)
sessionobj.commit()
sessionobj.close()
