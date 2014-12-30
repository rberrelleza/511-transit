from model import Model
from departure import Departure

class Stop(Model):
	def __init__(self, token, name, code):
		super(Stop, self).__init__(token)
		self._name = name
		self._code = str(code)

	@property
	def name(self):
	    return self._name
	
	@name.setter
	def name(self, value):
	    self._name = value
	
	@property
	def code(self):
	    return self._code
	
	@code.setter
	def code(self, value):
	    self._code = str(value)

	def __str__(self):
		return "{name} | {code} ".format(name=self.name, code=self.code)	
	
	def next_departures(self, route_code, direction=None):
		tree = self.get("GetNextDeparturesByStopCode.aspx", dict(stopCode=self.code))
		departure = Departure(route_code, self.code, direction)

		for route in tree[0][0][0]:
			if route.attrib["Code"] == str(route_code):
				for d in route[0]:
					if not direction or direction == d.attrib["Code"]:
						for stop in d[0]:
							if stop.attrib["StopCode"] == self.code:
								assert(stop[0].tag == "DepartureTimeList")
								for d in stop[0]:
									assert(d.tag == "DepartureTime")
									departure.times.append(int(d.text))

		return departure