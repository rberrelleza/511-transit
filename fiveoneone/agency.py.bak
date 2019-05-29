from model import Model
from route import Route

class Agency(Model):
	def __init__(self, token, name, hasDirection, mode):
		super(Agency, self).__init__(token)
		self._name = name
		self._hasDirection = self.to_bool(hasDirection)
		self._mode = mode

	@property
	def name(self):
	    return self._name
	
	@name.setter
	def name(self, value):
	    self._name = value
	
	@property
	def hasDirection(self):
	    return self._hasDirection
	
	@hasDirection.setter
	def hasDirection(self, value):
	    self._hasDirection = value
	
	@property
	def mode(self):
	    return self._mode
	
	@mode.setter
	def mode(self, value):
	    self._mode = value
	
	def routes(self):
		tree = self.get("GetRoutesForAgency.aspx", {"agencyName": self.name})
		routes = []
		for route in tree[0][0][0].getchildren():
			assert(route.tag.lower() == "route")
			routes.append(Route(self.token, self.name, route.attrib["Name"], route.attrib["Code"], self.hasDirection))

		return routes

	def __str__(self):
		return "{name} | {hasDirection} | {mode}".format(name=self.name, hasDirection=self.hasDirection, mode=self.mode)

	@classmethod
	def agencies(cls, token):
		if not token:
			raise ValueError("Must provide a valid 511.org token")

		tree = Model(token).get('GetAgencies.aspx')
		agencies = []
		for agency in tree[0].getchildren():
			assert(agency.tag.lower() == "agency")
			agencies.append(Agency(token, agency.attrib["Name"], agency.attrib["HasDirection"], agency.attrib["Mode"]))

		return agencies



