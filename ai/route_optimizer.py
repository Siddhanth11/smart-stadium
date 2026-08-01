# ai/route_optimizer.py

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class RouteOptimizerAI:
    """
    Smart Stadium Route Optimizer AI
    """

    def __init__(self):

        logging.info(
            "Initializing Route Optimizer AI..."
        )

        # ---------------------------------
        # Stadium Locations
        # ---------------------------------

        self.locations = [

            "Gate A",
            "Gate B",
            "Gate C",
            "Gate D",

            "Parking P1",
            "Parking P2",

            "Food Court",

            "Medical Center",

            "Restroom",

            "Fan Zone",

            "VIP Lounge",

            "Seat A",

            "Seat B",

            "Seat C"

        ]

        # ---------------------------------
        # Default Distance
        # ---------------------------------

        self.default_distance = 250

        # ---------------------------------
        # Walking Speed
        # ---------------------------------

        self.walking_speed = 75

        # ---------------------------------
        # Route History
        # ---------------------------------

        self.history = []

        logging.info(
            "Route Optimizer AI Ready."
        )

    # ---------------------------------
    # Current Time
    # ---------------------------------

    def current_time(self):

        return datetime.now()

    # ---------------------------------
    # Check Location
    # ---------------------------------

    def location_exists(self, location):

        return location in self.locations

    # ---------------------------------
    # Available Locations
    # ---------------------------------

    def available_locations(self):

        return self.locations

    # ---------------------------------
    # Total Locations
    # ---------------------------------

    def total_locations(self):

        return len(self.locations)

    # ---------------------------------
    # Estimated Walking Time
    # ---------------------------------

    def walking_time(self, distance=None):

        if distance is None:
            distance = self.default_distance

        minutes = round(distance / self.walking_speed)

        return max(1, minutes)

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "status": "Healthy",

            "locations": self.total_locations(),

            "routes_generated": len(self.history)

        }

    # ---------------------------------
    # Statistics
    # ---------------------------------

    def statistics(self):

        return {

            "locations": self.total_locations(),

            "walking_speed": self.walking_speed,

            "default_distance": self.default_distance,

            "history": len(self.history)

        }

    # ---------------------------------
    # Reset History
    # ---------------------------------

    def reset_history(self):

        self.history.clear()

        logging.info(
            "Route history cleared."
        )

    # ---------------------------------
    # Summary
    # ---------------------------------

    def summary(self):

        return {

            "health": self.health(),

            "statistics": self.statistics()

        }
    # ---------------------------------
    # Find Shortest Route
    # ---------------------------------

    def shortest_route(
        self,
        start,
        destination
    ):

        if not self.location_exists(start):
            return {
                "success": False,
                "message": "Invalid start location."
            }

        if not self.location_exists(destination):
            return {
                "success": False,
                "message": "Invalid destination."
            }

        distance = self.default_distance

        route = {

            "start": start,

            "destination": destination,

            "distance": distance,

            "walking_time":
                self.walking_time(distance),

            "route": [
                start,
                "Main Corridor",
                destination
            ]

        }

        self.history.append(route)

        return route

    # ---------------------------------
    # Parking Route
    # ---------------------------------

    def parking_route(self, gate):

        return self.shortest_route(
            gate,
            "Parking P1"
        )

    # ---------------------------------
    # Food Court Route
    # ---------------------------------

    def food_court_route(self, location):

        return self.shortest_route(
            location,
            "Food Court"
        )

    # ---------------------------------
    # Medical Route
    # ---------------------------------

    def medical_route(self, location):

        return self.shortest_route(
            location,
            "Medical Center"
        )

    # ---------------------------------
    # Emergency Exit Route
    # ---------------------------------

    def emergency_route(self, location):

        return {

            "start": location,

            "destination": "Gate A",

            "priority": "High",

            "distance": 120,

            "walking_time": 2,

            "route": [
                location,
                "Emergency Corridor",
                "Gate A"
            ]

        }

    # ---------------------------------
    # Least Crowded Route
    # ---------------------------------

    def least_crowded_route(
        self,
        start,
        destination
    ):

        return {

            "start": start,

            "destination": destination,

            "recommended_route": [

                start,

                "Side Corridor",

                destination

            ],

            "crowd_level": "Low",

            "distance": 280,

            "walking_time": 4

        }

    # ---------------------------------
    # Route History
    # ---------------------------------

    def route_history(self):

        return self.history

    # ---------------------------------
    # Last Route
    # ---------------------------------

    def last_route(self):

        if not self.history:
            return None

        return self.history[-1]
    # ---------------------------------
    # Most Visited Destination
    # ---------------------------------

    def most_visited_destination(self):

        if not self.history:
            return None

        destinations = {}

        for route in self.history:

            destination = route["destination"]

            destinations[destination] = (
                destinations.get(destination, 0) + 1
            )

        place = max(
            destinations,
            key=destinations.get
        )

        return {

            "destination": place,

            "count": destinations[place]

        }

    # ---------------------------------
    # Route Analytics
    # ---------------------------------

    def analytics(self):

        return {

            "total_routes":
                len(self.history),

            "most_visited":
                self.most_visited_destination(),

            "locations":
                self.total_locations()

        }

    # ---------------------------------
    # AI Recommendation
    # ---------------------------------

    def recommendation(self, destination):

        recommendations = {

            "Food Court":
                "Visit before halftime to avoid crowds.",

            "Parking P1":
                "Use Parking P2 if P1 becomes full.",

            "Medical Center":
                "Follow emergency signs for the fastest route.",

            "Fan Zone":
                "Recommended before the match begins."

        }

        return recommendations.get(
            destination,
            "Use the shortest available route."
        )

    # ---------------------------------
    # Dashboard
    # ---------------------------------

    def dashboard(self):

        return {

            "statistics":
                self.statistics(),

            "analytics":
                self.analytics(),

            "recent_route":
                self.last_route()

        }

    # ---------------------------------
    # Export Report
    # ---------------------------------

    def export(self):

        return {

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "statistics":
                self.statistics(),

            "analytics":
                self.analytics(),

            "history":
                self.route_history()

        }

    # ---------------------------------
    # AI Insights
    # ---------------------------------

    def insights(self):

        insights = []

        if not self.history:

            insights.append(
                "No routes have been generated yet."
            )

            return insights

        popular = self.most_visited_destination()

        insights.append(

            f"Most visited destination: "
            f"{popular['destination']}"

        )

        insights.append(

            f"Total routes generated: "
            f"{len(self.history)}"

        )

        insights.append(
            "Recommend least crowded routes during peak hours."
        )

        return insights

    # ---------------------------------
    # Complete Summary
    # ---------------------------------

    def complete_summary(self):

        return {

            "health":
                self.health(),

            "statistics":
                self.statistics(),

            "analytics":
                self.analytics(),

            "insights":
                self.insights()

        }

    # ---------------------------------
    # Reset Module
    # ---------------------------------

    def reset(self):

        self.reset_history()

        logging.info(
            "Route Optimizer AI reset."
        )

        return {

            "success": True,

            "message":
                "Route history cleared."

        }