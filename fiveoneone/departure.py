class Departure(object):
	def __init__(self, route, stop, direction=None, times=None):
		self._route = route
		self._stop = stop
		self._direction = direction
		if times:
			self._times = times
		else:
			self._times = []
		
	@property
	def route(self):
	     return self._route
	 
	@route.setter
	def route(self, value):
		self._route = value

	@property
	def stop(self):
	 	return self._stop

	@stop.setter
	def stop(self, value):
	 	self._stop = value

	@property
	def times(self):
	 	return self._times

	@times.setter
	def times(self, value):
	 	self._times = value

	@property
	def direction(self):
	    return self._direction
	
	@direction.setter
	def direction(self, value):
	    self._direction = value
	