import requests
from xml.etree import ElementTree

from model import Model
from stop import Stop

class Route(Model):

	OUTBOUND="Outbound"
	INBOUND="Inbound"

	def __init__(self, token, agency, name, code, direction=False):
		super(Route, self).__init__(token)
		self._name = name
		self._code = code
		self._agency = agency
		self._direction = direction

	@property
	def agency(self):
	    return self._agency
	
	@agency.setter
	def agency(self, value):
	    self._agency = value
	
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
	    self._code = value

	@property
	def direction(self):
	    return self._direction
	
	@direction.setter
	def direction(self, value):
	    self._direction = value

	def __str__(self):
		return "{name} | {code} | {direction} | {agency}".format(name=self.name, code=self.code, direction=self.direction, agency=self.agency)	
	
	def stops(self, direction=None):
		if self.direction:
			if direction not in [self.INBOUND, self.OUTBOUND]:
				raise ValueError("direction must be either {inboud} or {outbound}".format(inbound=INBOUND, outbound=OUTBOUND))
			url = 'http://services.my511.org/Transit2.0/GetStopsForRoute.aspx?token={token}&routeIDF={agency}~{code}~{direction}'.format(token=self.token, agency=self.agency, code=self.code, direction=direction)
		else:
			url = 'http://services.my511.org/Transit2.0/GetStopsForRoute.aspx?token={token}&routeIDF={agency}~{code}'.format(token=self.token, agency=self.agency, code=self.code)

		response = requests.get(url)
		response.raise_for_status()
		tree = ElementTree.fromstring(response.content)
		stops = []
		for stop in tree[0][0][0][0][0][0][0].getchildren():
			assert(stop.tag.lower() == "stop")
			stops.append(Stop(self.token, stop.attrib["name"], stop.attrib["StopCode"]))

		return stops
