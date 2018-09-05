from flask import Flask
from flask.json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import settings
import random


__db = None
__app = None


class Encoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "serialize"):
            return obj.serialize()
        return super(Encoder, self).default(obj)

def get_app():
    global __db, __api, __app
    __app = Flask(__name__)
    CORS(__app)
    __app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
    __app.json_encoder = Encoder
    __db = SQLAlchemy(__app)
    return __app

def get_db():
    global __db
    if not __db:
        get_app()
    return __db

def generate_id(length=8):
    __str = '1234567890qwertyuiopasdfghjklzxcvbnm'
    return ''.join(map(lambda x: __str[x], [random.randint(0, len(__str)-1) for i in range(length)]))
