from flask import request
from exceptions import BaseError, ErrValidate, ErrParam
import json


class Validater(object):

	def __init__(self):
		self.validates = []

	def add(self, validate):
		self.validates.append(validate)

	def run(self):
		return map(lambda x:x.run(), self.validates)


class MinxValidate(object):
	def __init__(self, default="", required=False):
		if required:
			self.default = None
		else:
			self.default = default

	@property
	def data(self):
		if request.method == "GET":
			self._data = request.args
		else:
			try:
				self._data = json.loads(request.get_data())
			except ValueError:
				raise ErrParam("Param isn't json")
		return self._data



class StringValidate(MinxValidate):
	def __init__(self, name, validate_func=None, *args, **kwargs):
		self.name = name
		self.validate_func = validate_func
		super().__init__(*args, **kwargs)


	def run(self):
		_data = self.data.get(self.name, self.default)
		if self.validate_func:
			_data = self.validate_func(_data)
		if _data == None:
			raise ErrParam("Param {0} required".format(self.name))
		if _data or _data == self.default:
			return _data
		raise ErrValidate("Can't get param {0}".format(self.name))


class NumberValidate(MinxValidate):
	def __init__(self, name, min=None, max=None, *args, **kwargs):
		self.name = name
		self.min = min
		self.max = max
		super().__init__(*args, **kwargs)

	def run(self):
		try:
			_data = int(self.data.get(self.name, self.default))
		except ValueError:
			raise ErrParam("{0}".format(self.name))
		if _data == None:
			raise ErrParam("Param {0} required".format(self.name))
		if self.min and _data < self.min:
			raise ErrValidate("{0} param < {1}(min).".format(self.name, self.min))
		if self.max and _data > self.max:
			raise ErrValidate("{0} param > {1}(max).".format(self.name, self.max))
		return _data