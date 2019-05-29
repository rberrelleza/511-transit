import requests
import urllib.parse
import urllib.request, urllib.parse, urllib.error
from xml.etree import ElementTree

from .exceptions import TransitServiceError, TokenRequired, InvalidToken, AgencyRequired, InvalidAgency, \
    InvalidRouteIDF, RouteIDFRequired, StopCodeRequired

class Model(object):
    def __init__(self, token):
        self._token = token
        self._base_uri = "http://services.my511.org/Transit2.0"

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

    def str_equals(self, str1, str2):
        return str1.lower().strip() == str2.lower().strip()

    def to_exception(self, error_tree):
         if not self.is_exception(error_tree) or not error_tree.text:
             raise ValueError("The value passed is not a valid error response")
         
         if self.str_equals(error_tree.text, "Token is required"):
             return TokenRequired()
         elif self.str_equals(error_tree.text, "Invalid credentials"):
             return InvalidToken()
         elif self.str_equals(error_tree.text, "Agency is required"):
             return AgencyRequired()
         elif self.str_equals(error_tree.text, "The Agency name is Invalid"):
             return InvalidAgency()
         elif self.str_equals(error_tree.text, "Invalid routeIDF"):
             return InvalidRouteIDF()
         elif self.str_equals(error_tree.text, "routeIDF is required"):
             return RouteIDFRequired()
         elif self.str_equals(error_tree.text, "stopCode is required"):
             return StopCodeRequired()
         else:
             return TransitServiceError()

    def is_exception(self, tree):
         return tree.tag.lower() == "transitserviceerror"

    def get(self, relative_path, parameters=None):
        if not parameters:
            parameters = dict()

        url = self._base_uri + "/" + relative_path.lstrip("/")
        parameters["token"] = self.token
        url = url + "?" + urllib.parse.urlencode(parameters)
        response = requests.get(url)
        response.raise_for_status()
        tree = ElementTree.fromstring(response.content)

        if self.is_exception(tree):
            raise self.to_exception(tree)

        return tree




