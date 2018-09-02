from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.json import JSONEncoder

_db = None


class Encoder(JSONEncoder):
	def default(self, obj):
		if hasattr(obj, "serialize"):
			return obj.serialize()
		return super(Encoder, self).default(obj)

def get_db():
	global _db
	if not _db:
		get_app()
	return _db

def get_app():
	global _db
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@172.16.29.32/zabbix'
	app.json_encoder = Encoder
	_db = SQLAlchemy(app)
	return app