import sqlalchemy as db

engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect()

metadata = db.MetaData()

movies = db.Table('Movies',metadata,autoload=True,autoload_with=engine)

query = db.select([movies])

result  = connection.execute(query)

print(result.fetchall())
