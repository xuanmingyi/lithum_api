from flask import Flask
from flask.json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy

import settings


__db = None


class Encoder(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "serialize"):
            return obj.serialize()
        return super(Encoder, self).default(obj)


def get_db():
    global __db
    if not __db:
        get_app()
    return __db


def get_app():
    global __db
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URI
    app.json_encoder = Encoder
    __db = SQLAlchemy(app)
    return app
