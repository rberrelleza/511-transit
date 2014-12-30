
class Model(object):
	def __init__(self, token):
		self._token = token

	@property
	def token(self):
	    return self._token

	def to_bool(self, value):
	 	if value == None:
	 		return False
	 	elif isinstance(value, bool):
	 		return value
	 	else:
	 		if str(value).lower() in ["true", "1", "yes"]:
	 			return True
	 		else:
	 			return False
