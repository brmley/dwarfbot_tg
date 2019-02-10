from peewee import ForeignKeyField, IntegerField, BooleanField
from db.models import BaseModel
from db.models.user import User
from db.models.session import Session


class UserSession(BaseModel):
    user = ForeignKeyField(User)
    session = ForeignKeyField(Session)
    position = IntegerField(primary_key=False)
    status = BooleanField(default=False)
