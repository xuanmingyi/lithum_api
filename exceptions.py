class BaseError(Exception):
	code = 0
	message = ""

	def __init__(self, message=""):
		if message:
			self.message += ": {0}".format(message)
		else:
			self.message += "."

	def decode_err(self):
		return self.code, self.message


class InternalServerError(BaseError):
	code = 10001
	message = "Internal server error"

class ErrValidate(BaseError):
	code = 20001
	message = "Validation failed"

class ErrParam(BaseError):
	code = 20003
	message = "Error param"

class ErrDatabase(BaseError):
	code = 20002
	message = "Database error"
