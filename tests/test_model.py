import unittest
import os

from xml.etree import ElementTree

from fiveoneone.model import Model
from fiveoneone.exceptions import TransitServiceError, TokenRequired, InvalidToken, AgencyRequired, InvalidAgency, \
	InvalidRouteIDF, RouteIDFRequired, StopCodeRequired

class TestAgency(unittest.TestCase):
	def setUp(self):
		self.model = Model("empty")

	def test_to_bool(self):
		self.assertEqual(self.model.to_bool(True), True)
		self.assertEqual(self.model.to_bool(False), False)
		self.assertEqual(self.model.to_bool("True"), True)
		self.assertEqual(self.model.to_bool("False"), False)
		self.assertEqual(self.model.to_bool("true"), True)
		self.assertEqual(self.model.to_bool("false"), False)
		self.assertEqual(self.model.to_bool("tRue"), True)
		self.assertEqual(self.model.to_bool("falsE"), False)
		self.assertEqual(self.model.to_bool(1), True)
		self.assertEqual(self.model.to_bool(0), False)
		self.assertEqual(self.model.to_bool("yes"), True)
		self.assertEqual(self.model.to_bool("no"), False)

	def test_is_exception(self):
		self.assertFalse(self.model.is_exception(ElementTree.fromstring("<RTT>test</RTT>")))
		self.assertTrue(self.model.is_exception(ElementTree.fromstring("<TransitServiceError>test</TransitServiceError>")))
		self.assertTrue(self.model.is_exception(ElementTree.fromstring("<TransitServiceError></TransitServiceError>")))

	def test_to_exception(self):
		self.assertRaises(ValueError, self.model.to_exception, ElementTree.fromstring("<RTT>test</RTT>"))
		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError>No match</TransitServiceError>")), 
			TransitServiceError)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError>Token is required</TransitServiceError>")), 
			TokenRequired)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError>Invalid credentials</TransitServiceError>")), 
			InvalidToken)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError> The Agency name is Invalid </TransitServiceError>")), 
			InvalidAgency)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError> Agency is required </TransitServiceError>")), 
			AgencyRequired)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError> routeIDF is required </TransitServiceError>")), 
			RouteIDFRequired)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError> Invalid routeIDF </TransitServiceError>")), 
			InvalidRouteIDF)

		self.assertIsInstance(self.model.to_exception(
			ElementTree.fromstring("<TransitServiceError> stopCode is required </TransitServiceError>")), 
			StopCodeRequired)
		