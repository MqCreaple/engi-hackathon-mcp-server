from MCP_server import *
import asyncio
import json
import sys

TEST_LOCATIONS = {
    "King's Cross": {"lat": 51.5308, "lon": -0.1238},
    "Camden Town": {"lat": 51.5390, "lon": -0.1426},
    "Baker Street": {"lat": 51.5224, "lon": -0.1578}
}

def test_location(loc: str, lat: float, lon: float):
    print("Location: ", loc)
    print("---  testing get_crime_summary  ---")
    print(get_crime_summary(lat, lon))
    print()
    print("---  testing get_time_context  ---")
    print(get_time_context(lat, lon))
    print()
    print("---  testing get_weather_conditions  ---")
    print(get_weather_conditions(lat, lon))
    print()

if __name__ == "__main__":
    for key, value in TEST_LOCATIONS.items():
        test_location(key, value["lat"], value["lon"])