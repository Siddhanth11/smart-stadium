# services/map_service.py

import math


class MapService:
    """
    Smart Stadium Map Service
    """

    def __init__(self):

        self.locations = {

            "Gate A": (0, 0),

            "Gate B": (0, 100),

            "Gate C": (100, 0),

            "Gate D": (100, 100),

            "Parking": (200, 50),

            "Food Court": (50, 50),

            "Medical Center": (150, 30),

            "Fan Zone": (80, 80),

            "Seat A": (40, 60),

            "Seat B": (60, 70),

            "Seat C": (70, 40)

        }

    # ---------------------------------
    # Check Location
    # ---------------------------------

    def location_exists(self, location):

        return location in self.locations

    # ---------------------------------
    # Get Coordinates
    # ---------------------------------

    def coordinates(self, location):

        return self.locations.get(location)

    # ---------------------------------
    # Distance Between Two Locations
    # ---------------------------------

    def distance(
        self,
        source,
        destination
    ):

        if not self.location_exists(source):
            return None

        if not self.location_exists(destination):
            return None

        x1, y1 = self.locations[source]

        x2, y2 = self.locations[destination]

        return round(
            math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            ),
            2
        )

    # ---------------------------------
    # Route
    # ---------------------------------

    def route(
        self,
        source,
        destination
    ):

        if not self.location_exists(source):
            return {
                "success": False,
                "message": "Invalid source."
            }

        if not self.location_exists(destination):
            return {
                "success": False,
                "message": "Invalid destination."
            }

        return {

            "source": source,

            "destination": destination,

            "distance":
                self.distance(
                    source,
                    destination
                ),

            "estimated_time":
                "3 minutes",

            "path": [

                source,

                "Main Corridor",

                destination

            ]

        }

    # ---------------------------------
    # Nearby Locations
    # ---------------------------------

    def nearby(self, location):

        if not self.location_exists(location):

            return []

        nearby_places = []

        for place in self.locations:

            if place != location:

                nearby_places.append(place)

        return nearby_places[:5]

    # ---------------------------------
    # Parking Route
    # ---------------------------------

    def parking_route(self, location):

        return self.route(
            location,
            "Parking"
        )

    # ---------------------------------
    # Medical Route
    # ---------------------------------

    def medical_route(self, location):

        return self.route(
            location,
            "Medical Center"
        )

    # ---------------------------------
    # Food Court Route
    # ---------------------------------

    def food_route(self, location):

        return self.route(
            location,
            "Food Court"
        )

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "service": "Map Service",

            "locations":
                len(self.locations),

            "status": "Running"

        }


# Singleton Object

map_service = MapService()