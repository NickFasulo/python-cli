from peewee import *
import datetime

db = PostgresqlDatabase('bookmarks', user='postgres', password='12345',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Bookmark(BaseModel):
    name = CharField(unique=True)
    link = CharField(unique=True)

# date = datetime.date

# db.drop_tables(Bookmark)
# db.create_tables(Bookmark)
