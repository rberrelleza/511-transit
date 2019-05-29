
import unittest
import os
from fiveoneone.agency import Agency
from fiveoneone.route import Route
from fiveoneone.stop import Stop

class TestAgency(unittest.TestCase):

	def setUp(self):
		if "FIVEONEONE_TOKEN" not in os.environ:
			raise Exception("FIVEONEONE_TOKEN environment variable must be set before running the tests")

		self.token = os.environ["FIVEONEONE_TOKEN"]

	def test_agencies(self):
		agencies = Agency.agencies(self.token)
		self.assertIsNotNone(agencies)
		self.assertTrue(len(agencies) > 0)
		
		found_muni = False
		for agency in agencies:
			self.assertIsNotNone(agency.name)
			self.assertIsNotNone(agency.hasDirection)
			self.assertIsNotNone(agency.mode)
			if agency.name == "SFMTA":
				found_muni = True
		self.assertTrue(found_muni)

	def test_routes(self):
		agency = Agency(self.token, "SFMTA", "True", "Bus")
		routes = agency.routes()
		self.assertIsNotNone(routes)

	def test_stops(self):
		route = Route(self.token, "SFMTA", "41-Union", "41", True)
		stops = route.stops(Route.INBOUND)
		self.assertIsNotNone(stops)
		for s in stops:
			self.assertIsNotNone(s.name)
			self.assertIsNotNone(s.code)

		outbound_stops = route.stops(Route.OUTBOUND)
		self.assertIsNotNone(outbound_stops)
		for s in outbound_stops:
			self.assertIsNotNone(s.name)
			self.assertIsNotNone(s.code)	

	def test_departures(self):
		route = Route(self.token, "SFMTA", "45-Union Stockton", "45", True)
		stop = Stop(self.token, "Union St and Buchanan St", "17056")
		departures = stop.next_departures(route.code)
		self.assertIsNotNone(departures)
		self.assertEqual(departures.route, route.code)
		self.assertTrue(len(departures.times) > 0)
		for time in departures.times:
			self.assertIsNotNone(time)

		outbound_departures = stop.next_departures(route.code, direction=route.OUTBOUND)
		self.assertIsNotNone(outbound_departures)
		self.assertEqual(outbound_departures.route, route.code)
		self.assertTrue(len(outbound_departures.times) > 0)
		for time in outbound_departures.times:
			self.assertIsNotNone(time)
