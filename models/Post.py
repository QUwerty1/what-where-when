import datetime
from peewee import *
from models.BaseModel import BaseModel


class Post(BaseModel):
    post_id = PrimaryKeyField()
    title = CharField()
    img = CharField()
    text = TextField()
    created_at = DateTimeField()

    class Meta:
        db_table = "Posts"
