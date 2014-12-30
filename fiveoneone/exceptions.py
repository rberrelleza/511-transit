class TransitServiceError(Exception):
	pass

class TokenRequired(TransitServiceError):
	pass

class InvalidToken(TransitServiceError):
	pass

class AgencyRequired(TransitServiceError):
	pass

class InvalidAgency(TransitServiceError):
	pass

class InvalidRouteIDF(TransitServiceError):
	pass

class RouteIDFRequired(TransitServiceError):
	pass

class StopCodeRequired(TransitServiceError):
	pass