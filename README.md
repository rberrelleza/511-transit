511-transit
===========

Python API to consume transit data from http://511.org. 

In order to use this library, you will need to signup for a [511.org developer token](http://511.org/developer-resources_transit-api.asp). 

## Sample usage
``` python
from fiveoneone.route import Route
from fiveoneone.stop import Stop

token = "YOUR_DEVELOPER_TOKEN"
route = Route(token, "SFMTA", "45-Union Stockton", "45", True)
stop = Stop(token, "Union St and Buchanan St", "17056")
departures = stop.next_departures(route.code, "Outbound")
print "{} Outbound will arrive to {} in {} minutes".format(route.code, stop.name, departures.times[0])
# 45 Outbound will to Union St and Buchanan St in 5 minutes
```

* See the tests/test_integration.py for other usages.

## Run the tests
requirements.dev.txt has all the requirements to run the tests. After that, from the repo root do to run all the available tests:
```
nosetests
```
