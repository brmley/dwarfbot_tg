import re
from peewee import IntegerField, TextField, ForeignKeyField, BooleanField

from db.models import BaseModel
from db.models.user import User


class Session(BaseModel):
    id = IntegerField(primary_key=True)
    name = TextField()
    curator = ForeignKeyField(User)
    chat = IntegerField()
    status = BooleanField(null=True)
    description = TextField(null=True)
    cloud_doc = TextField(null=True)
    cloud_dir = TextField(null=True)

    def hashtag(self):
        regex = re.compile('[^a-zA-Z]')
        return '#'+regex.sub('', self.name)
