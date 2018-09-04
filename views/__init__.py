from flask.views import MethodView
from exceptions import BaseError
from flask import jsonify


class APIView(MethodView):
	def dispatch_request(self, *args, **kwargs):
		try:
			data = super(APIView, self).dispatch_request(*args, **kwargs)
			code = 200
			message = 'ok'
		except BaseError as e:
			code, message = e.decode_err()
			data = None
		return jsonify({
			'code': code,
			'message': message,
			'data': data
		})
