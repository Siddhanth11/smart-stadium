# ai/crowd_detection.py

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class CrowdDetectionAI:

    def __init__(self):

        logging.info(
            "Initializing Crowd Detection AI..."
        )

        # Crowd information
        self.zones = {}

        self.alerts = []

        self.history = []

        # Thresholds
        self.thresholds = {
            "Low": 30,
            "Medium": 60,
            "High": 85,
            "Critical": 100
        }

        self.statistics = {}

        self.load_zones()

        logging.info(
            "Crowd Detection AI Ready."
        )

    # -----------------------------
    # Time
    # -----------------------------

    def current_time(self):

        return datetime.now()

    # -----------------------------
    # Load Stadium Zones
    # -----------------------------

    def load_zones(self):

        self.zones = {

            "Gate A": {
                "capacity": 1000,
                "people": 0
            },

            "Gate B": {
                "capacity": 1000,
                "people": 0
            },

            "Gate C": {
                "capacity": 1000,
                "people": 0
            },

            "Gate D": {
                "capacity": 1000,
                "people": 0
            },

            "Food Court": {
                "capacity": 500,
                "people": 0
            },

            "Parking": {
                "capacity": 2000,
                "people": 0
            }

        }

    # -----------------------------
    # Available Zones
    # -----------------------------

    def zone_list(self):

        return list(self.zones.keys())

    # -----------------------------
    # Zone Exists
    # -----------------------------

    def zone_exists(self, zone):

        return zone in self.zones

    # -----------------------------
    # Health
    # -----------------------------

    def health(self):

        return {

            "status": "Healthy",

            "zones": len(self.zones),

            "alerts": len(self.alerts)

        }
    # -------------------------------------
    # Zone Information
    # -------------------------------------

    def zone_info(self, zone):

        if not self.zone_exists(zone):
            return None

        return self.zones[zone]

    # -------------------------------------
    # Zone Capacity
    # -------------------------------------

    def capacity(self, zone):

        info = self.zone_info(zone)

        if info:
            return info["capacity"]

        return 0

    # -------------------------------------
    # Current Crowd
    # -------------------------------------

    def current_people(self, zone):

        info = self.zone_info(zone)

        if info:
            return info["people"]

        return 0

    # -------------------------------------
    # Occupancy Percentage
    # -------------------------------------

    def occupancy_percentage(self, zone):

        if not self.zone_exists(zone):
            return 0

        people = self.current_people(zone)

        capacity = self.capacity(zone)

        if capacity == 0:
            return 0

        return round((people / capacity) * 100, 2)

    # -------------------------------------
    # Crowd Level
    # -------------------------------------

    def crowd_level(self, zone):

        percentage = self.occupancy_percentage(zone)

        if percentage <= self.thresholds["Low"]:
            return "Low"

        elif percentage <= self.thresholds["Medium"]:
            return "Medium"

        elif percentage <= self.thresholds["High"]:
            return "High"

        return "Critical"

    # -------------------------------------
    # Total Capacity
    # -------------------------------------

    def total_capacity(self):

        total = 0

        for zone in self.zones.values():
            total += zone["capacity"]

        return total

    # -------------------------------------
    # Total People
    # -------------------------------------

    def total_people(self):

        total = 0

        for zone in self.zones.values():
            total += zone["people"]

        return total

    # -------------------------------------
    # Overall Occupancy
    # -------------------------------------

    def overall_occupancy(self):

        capacity = self.total_capacity()

        if capacity == 0:
            return 0

        return round(
            (self.total_people() / capacity) * 100,
            2
        )

    # -------------------------------------
    # Crowd Statistics
    # -------------------------------------

    def statistics(self):

        return {

            "zones": len(self.zones),

            "total_capacity": self.total_capacity(),

            "total_people": self.total_people(),

            "overall_occupancy":
                self.overall_occupancy(),

            "active_alerts":
                len(self.alerts)

        }

    # -------------------------------------
    # Reset Crowd
    # -------------------------------------

    def reset(self):

        for zone in self.zones:

            self.zones[zone]["people"] = 0

        self.alerts.clear()

        self.history.clear()

        logging.info(
            "Crowd statistics reset."
        )
    # -------------------------------------
    # Update Crowd Count
    # -------------------------------------

    def update_crowd(self, zone, people):

        if not self.zone_exists(zone):

            return {
                "success": False,
                "message": "Invalid zone."
            }

        self.zones[zone]["people"] = people

        self.history.append({

            "zone": zone,

            "people": people,

            "time": self.current_time()

        })

        return {

            "success": True,

            "zone": zone,

            "people": people,

            "level": self.crowd_level(zone)

        }

    # -------------------------------------
    # Increase Crowd
    # -------------------------------------

    def add_people(self, zone, count):

        if not self.zone_exists(zone):
            return False

        self.zones[zone]["people"] += count

        return True

    # -------------------------------------
    # Decrease Crowd
    # -------------------------------------

    def remove_people(self, zone, count):

        if not self.zone_exists(zone):
            return False

        current = self.zones[zone]["people"]

        self.zones[zone]["people"] = max(
            0,
            current - count
        )

        return True

    # -------------------------------------
    # Check Alerts
    # -------------------------------------

    def check_alerts(self):

        self.alerts.clear()

        for zone in self.zones:

            level = self.crowd_level(zone)

            if level in ["High", "Critical"]:

                self.alerts.append({

                    "zone": zone,

                    "level": level,

                    "occupancy":
                        self.occupancy_percentage(zone),

                    "time":
                        self.current_time()

                })

        return self.alerts

    # -------------------------------------
    # Heatmap
    # -------------------------------------

    def heatmap(self):

        heat = {}

        for zone in self.zones:

            heat[zone] = {

                "people":
                    self.current_people(zone),

                "occupancy":
                    self.occupancy_percentage(zone),

                "level":
                    self.crowd_level(zone)

            }

        return heat

    # -------------------------------------
    # Most Crowded Zone
    # -------------------------------------

    def busiest_zone(self):

        if not self.zones:
            return None

        return max(

            self.zones,

            key=lambda zone:
                self.current_people(zone)

        )

    # -------------------------------------
    # Least Crowded Zone
    # -------------------------------------

    def least_busy_zone(self):

        if not self.zones:
            return None

        return min(

            self.zones,

            key=lambda zone:
                self.current_people(zone)

        )

    # -------------------------------------
    # Live Dashboard
    # -------------------------------------

    def dashboard(self):

        return {

            "statistics":
                self.statistics(),

            "busiest_zone":
                self.busiest_zone(),

            "least_busy_zone":
                self.least_busy_zone(),

            "alerts":
                self.check_alerts(),

            "heatmap":
                self.heatmap()

        }
    # -------------------------------------
    # Predict Crowd
    # -------------------------------------

    def predict_crowd(self, zone):

        if not self.zone_exists(zone):

            return None

        current = self.current_people(zone)

        prediction = int(current * 1.10)

        return {

            "zone": zone,

            "current": current,

            "predicted": prediction

        }

    # -------------------------------------
    # Congestion Risk
    # -------------------------------------

    def congestion_risk(self, zone):

        if not self.zone_exists(zone):

            return "Unknown"

        occupancy = self.occupancy_percentage(zone)

        if occupancy < 40:
            return "Low"

        elif occupancy < 70:
            return "Medium"

        elif occupancy < 90:
            return "High"

        return "Critical"

    # -------------------------------------
    # AI Recommendation
    # -------------------------------------

    def recommendation(self, zone):

        risk = self.congestion_risk(zone)

        if risk == "Low":
            return "No action required."

        elif risk == "Medium":
            return "Monitor crowd movement."

        elif risk == "High":
            return "Deploy additional volunteers."

        return "Open alternative gates immediately."

    # -------------------------------------
    # Zone Report
    # -------------------------------------

    def zone_report(self, zone):

        if not self.zone_exists(zone):

            return None

        return {

            "zone": zone,

            "people": self.current_people(zone),

            "capacity": self.capacity(zone),

            "occupancy":
                self.occupancy_percentage(zone),

            "level":
                self.crowd_level(zone),

            "risk":
                self.congestion_risk(zone),

            "recommendation":
                self.recommendation(zone)

        }

    # -------------------------------------
    # Full Report
    # -------------------------------------

    def report(self):

        reports = []

        for zone in self.zone_list():

            reports.append(
                self.zone_report(zone)
            )

        return reports

    # -------------------------------------
    # Export Data
    # -------------------------------------

    def export(self):

        return {

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "statistics":
                self.statistics(),

            "heatmap":
                self.heatmap(),

            "reports":
                self.report()

        }

    # -------------------------------------
    # AI Insights
    # -------------------------------------

    def insights(self):

        busiest = self.busiest_zone()

        return [

            f"Most crowded zone: {busiest}",

            f"Overall occupancy: {self.overall_occupancy()}%",

            "Continue monitoring high-density areas."

        ]

    # -------------------------------------
    # System Summary
    # -------------------------------------

    def summary(self):

        return {

            "health": self.health(),

            "statistics": self.statistics(),

            "alerts": self.check_alerts(),

            "insights": self.insights()

        }
