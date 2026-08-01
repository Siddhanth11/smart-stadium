"""
ai/navigation_ai.py
Smart Stadium GenAI Navigation Module
"""

import math
import heapq
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class NavigationAI:
    """
    AI-powered stadium navigation system.
    """

    def __init__(self):

        logging.info("Initializing Navigation AI...")

        # Graph
        # Format:
        # {
        #   "Gate A": {
        #       "Parking A": 40,
        #       "Food Court": 60
        #   }
        # }

        self.graph = {}

        # Coordinates
        # Format:
        # {
        #   "Gate A": (10,20)
        # }

        self.coordinates = {}

        # Facility categories

        self.gates = []
        self.parking = []
        self.food_courts = []
        self.washrooms = []
        self.medical = []
        self.exits = []
        self.seating = []
        self.shops = []

        # Load map

        self.load_locations()
        self.load_graph()

        logging.info("Navigation AI Ready")

    # -----------------------------------

    def load_locations(self):
        """
        Placeholder.
        Filled in Part 1B.
        """

        pass

    # -----------------------------------

    def load_graph(self):
        """
        Placeholder.
        Filled in Part 1C.
        """

        pass

    # -----------------------------------

    def add_location(
        self,
        name,
        x,
        y,
        category
    ):
        """
        Add a location to the navigation map.
        """

        self.coordinates[name] = (x, y)

        if category == "gate":
            self.gates.append(name)

        elif category == "parking":
            self.parking.append(name)

        elif category == "food":
            self.food_courts.append(name)

        elif category == "washroom":
            self.washrooms.append(name)

        elif category == "medical":
            self.medical.append(name)

        elif category == "exit":
            self.exits.append(name)

        elif category == "seat":
            self.seating.append(name)

        elif category == "shop":
            self.shops.append(name)

    # -----------------------------------

    def add_edge(
        self,
        source,
        destination,
        distance
    ):
        """
        Create a bidirectional path.
        """

        self.graph.setdefault(source, {})
        self.graph.setdefault(destination, {})

        self.graph[source][destination] = distance
        self.graph[destination][source] = distance

    # -----------------------------------

    def get_all_locations(self):
        """
        Return all known locations.
        """

        return sorted(self.coordinates.keys())

    # -----------------------------------

    def location_exists(
        self,
        location
    ):

        return location in self.coordinates

    # -----------------------------------

    def get_coordinate(
        self,
        location
    ):

        return self.coordinates.get(location)

    # -----------------------------------

    def distance_between(
        self,
        point1,
        point2
    ):
        """
        Euclidean distance between two coordinates.
        """

        if point1 not in self.coordinates:
            return None

        if point2 not in self.coordinates:
            return None

        x1, y1 = self.coordinates[point1]
        x2, y2 = self.coordinates[point2]

        return round(
            math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            ),
            2
        )

    # -----------------------------------

    def stadium_summary(self):

        return {

            "locations": len(self.coordinates),

            "gates": len(self.gates),

            "parking": len(self.parking),

            "food_courts": len(self.food_courts),

            "washrooms": len(self.washrooms),

            "medical": len(self.medical),

            "emergency_exits": len(self.exits),

            "seating_blocks": len(self.seating)

        }
def load_locations(self):
    """
    Load stadium locations with coordinates.
    Coordinates are virtual (x, y) values used by the
    routing algorithm.
    """

    # ===================================================
    # GATES
    # ===================================================

    self.add_location(
        "Gate A",
        10,
        50,
        "gate"
    )

    self.add_location(
        "Gate B",
        30,
        90,
        "gate"
    )

    self.add_location(
        "Gate C",
        70,
        90,
        "gate"
    )

    self.add_location(
        "Gate D",
        90,
        50,
        "gate"
    )

    self.add_location(
        "Gate E",
        70,
        10,
        "gate"
    )

    self.add_location(
        "Gate F",
        30,
        10,
        "gate"
    )

    # ===================================================
    # PARKING
    # ===================================================

    self.add_location(
        "Parking P1",
        5,
        55,
        "parking"
    )

    self.add_location(
        "Parking P2",
        25,
        95,
        "parking"
    )

    self.add_location(
        "Parking P3",
        75,
        95,
        "parking"
    )

    self.add_location(
        "Parking P4",
        95,
        55,
        "parking"
    )

    self.add_location(
        "Parking P5",
        50,
        5,
        "parking"
    )
    # ===================================================
    # SEATING BLOCKS (A–F)
    # ===================================================

    self.add_location(
        "Block A",
        30,
        70,
        "seat"
    )

    self.add_location(
        "Block B",
        40,
        70,
        "seat"
    )

    self.add_location(
        "Block C",
        50,
        70,
        "seat"
    )

    self.add_location(
        "Block D",
        60,
        70,
        "seat"
    )

    self.add_location(
        "Block E",
        35,
        55,
        "seat"
    )

    self.add_location(
        "Block F",
        55,
        55,
        "seat"
    )
    # ===================================================
    # SEATING BLOCKS (G–L)
    # ===================================================

    self.add_location(
        "Block G",
        30,
        40,
        "seat"
    )

    self.add_location(
        "Block H",
        40,
        40,
        "seat"
    )

    self.add_location(
        "Block I",
        50,
        40,
        "seat"
    )

    self.add_location(
        "Block J",
        60,
        40,
        "seat"
    )

    self.add_location(
        "Block K",
        35,
        25,
        "seat"
    )

    self.add_location(
        "Block L",
        55,
        25,
        "seat"
    )