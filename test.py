from MCP_server import *
import asyncio
import json
import sys

TEST_LOCATIONS = {
    "King's Cross": {"lat": 51.5308, "lon": -0.1238},
    "Camden Town": {"lat": 51.5390, "lon": -0.1426},
    "Baker Street": {"lat": 51.5224, "lon": -0.1578}
}


test=get_crime_summary(TEST_LOCATIONS["King's Cross"]["lat"], TEST_LOCATIONS["King's Cross"]["lon"])
print(test)