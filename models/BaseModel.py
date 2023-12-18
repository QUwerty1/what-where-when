from peewee import *
from os import environ


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase(environ.get("DB_CONN"))
