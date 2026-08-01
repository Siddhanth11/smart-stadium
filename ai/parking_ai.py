"""
Smart Stadium GenAI
Parking Recommendation AI
"""

import math
import random
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class ParkingAI:
    """
    AI Parking Recommendation System
    """

    def __init__(self):

        logging.info("Initializing Parking AI...")

        # Parking Zone Information
        self.parking_zones = {}

        # Live Occupancy
        self.occupancy = {}

        # Maximum Capacity
        self.capacity = {}

        # Coordinates
        self.coordinates = {}

        # Entry Gates
        self.nearest_gate = {}

        # Vehicle Types
        self.vehicle_types = [
            "Car",
            "Bike",
            "Bus",
            "VIP"
        ]

        # Dynamic Prices
        self.pricing = {}

        # Load Data
        self.load_parking_data()

        logging.info("Parking AI Ready")

    # ---------------------------------

    def load_parking_data(self):
        """
        Placeholder.
        Filled in Part 1B.
        """
        pass

    # ---------------------------------

    def current_time(self):

        return datetime.now()

    # ---------------------------------

    def total_capacity(self):

        return sum(self.capacity.values())

    # ---------------------------------

    def occupied_spaces(self):

        return sum(self.occupancy.values())

    # ---------------------------------

    def available_spaces(self):

        return self.total_capacity() - self.occupied_spaces()

    # ---------------------------------

    def parking_summary(self):

        return {

            "zones": len(self.parking_zones),

            "capacity": self.total_capacity(),

            "occupied": self.occupied_spaces(),

            "available": self.available_spaces()

        }

    # ---------------------------------

    def zone_exists(self, zone):

        return zone in self.parking_zones

    # ---------------------------------

    def get_zone(self, zone):

        return self.parking_zones.get(zone)

    # ---------------------------------

    def occupancy_percentage(self, zone):

        if zone not in self.capacity:
            return 0

        return round(

            (
                self.occupancy[zone]
                /
                self.capacity[zone]
            ) * 100,

            2

        )
def load_parking_data(self):
    """
    Initialize standard parking zones.
    """

    # -------------------------------
    # Parking Zone P1
    # -------------------------------

    self.parking_zones["P1"] = {
        "name": "Parking Zone P1",
        "type": "Standard"
    }

    self.capacity["P1"] = 250
    self.occupancy["P1"] = 95
    self.coordinates["P1"] = (5, 55)
    self.nearest_gate["P1"] = "Gate A"
    self.pricing["P1"] = 100

    # -------------------------------
    # Parking Zone P2
    # -------------------------------

    self.parking_zones["P2"] = {
        "name": "Parking Zone P2",
        "type": "Standard"
    }

    self.capacity["P2"] = 300
    self.occupancy["P2"] = 140
    self.coordinates["P2"] = (25, 95)
    self.nearest_gate["P2"] = "Gate B"
    self.pricing["P2"] = 120

    # -------------------------------
    # Parking Zone P3
    # -------------------------------

    self.parking_zones["P3"] = {
        "name": "Parking Zone P3",
        "type": "Standard"
    }

    self.capacity["P3"] = 350
    self.occupancy["P3"] = 175
    self.coordinates["P3"] = (75, 95)
    self.nearest_gate["P3"] = "Gate C"
    self.pricing["P3"] = 120

    # -------------------------------
    # Parking Zone P4
    # -------------------------------

    self.parking_zones["P4"] = {
        "name": "Parking Zone P4",
        "type": "Standard"
    }

    self.capacity["P4"] = 250
    self.occupancy["P4"] = 110
    self.coordinates["P4"] = (95, 55)
    self.nearest_gate["P4"] = "Gate D"
    self.pricing["P4"] = 100

    # -------------------------------
    # Parking Zone P5
    # -------------------------------

    self.parking_zones["P5"] = {
        "name": "Parking Zone P5",
        "type": "Standard"
    }

    self.capacity["P5"] = 200
    self.occupancy["P5"] = 60
    self.coordinates["P5"] = (50, 5)
    self.nearest_gate["P5"] = "Gate E"
    self.pricing["P5"] = 80
    # -------------------------------
    # VIP Parking
    # -------------------------------

    self.parking_zones["VIP"] = {
        "name": "VIP Parking",
        "type": "VIP"
    }

    self.capacity["VIP"] = 80
    self.occupancy["VIP"] = 22
    self.coordinates["VIP"] = (48, 92)
    self.nearest_gate["VIP"] = "Gate B"
    self.pricing["VIP"] = 500

    # -------------------------------
    # Bus Parking
    # -------------------------------

    self.parking_zones["BUS"] = {
        "name": "Bus Parking",
        "type": "Bus"
    }

    self.capacity["BUS"] = 40
    self.occupancy["BUS"] = 15
    self.coordinates["BUS"] = (98, 75)
    self.nearest_gate["BUS"] = "Gate D"
    self.pricing["BUS"] = 300

    # -------------------------------
    # Bike Parking
    # -------------------------------

    self.parking_zones["BIKE"] = {
        "name": "Bike Parking",
        "type": "Bike"
    }

    self.capacity["BIKE"] = 500
    self.occupancy["BIKE"] = 180
    self.coordinates["BIKE"] = (8, 18)
    self.nearest_gate["BIKE"] = "Gate F"
    self.pricing["BIKE"] = 40

    logging.info(
        "Loaded %d parking zones.",
        len(self.parking_zones)
    )
    # ---------------------------------------------------
    # Available Spaces in a Zone
    # ---------------------------------------------------

    def available_in_zone(self, zone):
        """
        Returns available parking spaces in a zone.
        """

        if not self.zone_exists(zone):
            return 0

        return max(
            self.capacity[zone] -
            self.occupancy[zone],
            0
        )

    # ---------------------------------------------------
    # Check Zone Availability
    # ---------------------------------------------------

    def is_zone_available(self, zone):

        if not self.zone_exists(zone):
            return False

        return self.available_in_zone(zone) > 0

    # ---------------------------------------------------
    # Zone Occupancy Percentage
    # ---------------------------------------------------

    def zone_utilization(self, zone):

        if not self.zone_exists(zone):
            return 0

        return round(

            (
                self.occupancy[zone]
                /
                self.capacity[zone]
            ) * 100,

            2

        )

    # ---------------------------------------------------
    # Get All Available Zones
    # ---------------------------------------------------

    def get_available_zones(self):

        available = []

        for zone in self.parking_zones:

            if self.is_zone_available(zone):

                available.append({

                    "zone": zone,

                    "available": self.available_in_zone(zone),

                    "capacity": self.capacity[zone],

                    "occupied": self.occupancy[zone],

                    "utilization": self.zone_utilization(zone),

                    "gate": self.nearest_gate[zone],

                    "price": self.pricing[zone]

                })

        return available

    # ---------------------------------------------------
    # Zone Information
    # ---------------------------------------------------

    def zone_information(self, zone):

        if not self.zone_exists(zone):

            return None

        return {

            "zone": zone,

            "name": self.parking_zones[zone]["name"],

            "type": self.parking_zones[zone]["type"],

            "capacity": self.capacity[zone],

            "occupied": self.occupancy[zone],

            "available": self.available_in_zone(zone),

            "utilization": self.zone_utilization(zone),

            "gate": self.nearest_gate[zone],

            "price": self.pricing[zone],

            "coordinates": self.coordinates[zone]

        }

    # ---------------------------------------------------
    # List Zones by Type
    # ---------------------------------------------------

    def zones_by_type(self, parking_type):

        result = []

        for zone in self.parking_zones:

            if self.parking_zones[zone]["type"].lower() == parking_type.lower():

                result.append(zone)

        return result

    # ---------------------------------------------------
    # Parking Status
    # ---------------------------------------------------

    def parking_status(self):

        return {

            "summary": self.parking_summary(),

            "zones": self.get_available_zones(),

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }
    # ---------------------------------------------------
    # Reserve a Parking Slot
    # ---------------------------------------------------

    def reserve_slot(self, zone):
        """
        Reserve one parking space in the given zone.

        Returns:
            (True, message) on success
            (False, message) on failure
        """

        if not self.zone_exists(zone):
            return False, "Parking zone does not exist."

        if self.available_in_zone(zone) <= 0:
            return False, "Parking zone is full."

        self.occupancy[zone] += 1

        logging.info(
            "Reserved one slot in %s. Occupancy: %d/%d",
            zone,
            self.occupancy[zone],
            self.capacity[zone]
        )

        return True, f"Parking slot reserved in {zone}."

    # ---------------------------------------------------
    # Release a Parking Slot
    # ---------------------------------------------------

    def release_slot(self, zone):
        """
        Release one occupied parking slot.
        """

        if not self.zone_exists(zone):
            return False, "Parking zone does not exist."

        if self.occupancy[zone] <= 0:
            return False, "No occupied slot to release."

        self.occupancy[zone] -= 1

        logging.info(
            "Released one slot from %s. Occupancy: %d/%d",
            zone,
            self.occupancy[zone],
            self.capacity[zone]
        )

        return True, f"Parking slot released from {zone}."

    # ---------------------------------------------------
    # Update Occupancy
    # ---------------------------------------------------

    def update_occupancy(self, zone, occupied):
        """
        Set occupancy for a zone.

        Example:
            update_occupancy("P1", 120)
        """

        if not self.zone_exists(zone):
            return False, "Parking zone does not exist."

        if occupied < 0:
            occupied = 0

        if occupied > self.capacity[zone]:
            occupied = self.capacity[zone]

        self.occupancy[zone] = occupied

        logging.info(
            "Updated occupancy for %s to %d/%d",
            zone,
            occupied,
            self.capacity[zone]
        )

        return True, "Occupancy updated successfully."

    # ---------------------------------------------------
    # Occupy Multiple Slots
    # ---------------------------------------------------

    def occupy_slots(self, zone, count):
        """
        Increase occupancy by 'count' slots.
        """

        if not self.zone_exists(zone):
            return False

        if count <= 0:
            return False

        available = self.available_in_zone(zone)

        increase = min(count, available)

        self.occupancy[zone] += increase

        return True

    # ---------------------------------------------------
    # Free Multiple Slots
    # ---------------------------------------------------

    def free_slots(self, zone, count):
        """
        Free multiple occupied parking spaces.
        """

        if not self.zone_exists(zone):
            return False

        if count <= 0:
            return False

        decrease = min(count, self.occupancy[zone])

        self.occupancy[zone] -= decrease

        return True
    # ---------------------------------------------------
    # Reset Occupancy
    # ---------------------------------------------------

    def reset_occupancy(self):
        """
        Reset occupancy for all parking zones.
        """

        for zone in self.occupancy:
            self.occupancy[zone] = 0

        logging.info("All parking occupancy values have been reset.")

    # ---------------------------------------------------
    # Simulate Random Occupancy
    # ---------------------------------------------------

    def simulate_occupancy(self):
        """
        Randomly simulate occupancy for all parking zones.
        Useful for testing.
        """

        for zone in self.capacity:

            self.occupancy[zone] = random.randint(
                0,
                self.capacity[zone]
            )

        logging.info("Parking occupancy simulation completed.")

    # ---------------------------------------------------
    # Check if Parking is Full
    # ---------------------------------------------------

    def is_full(self, zone):
        """
        Returns True if the zone has no available spaces.
        """

        if not self.zone_exists(zone):
            return False

        return self.available_in_zone(zone) == 0

    # ---------------------------------------------------
    # Check if Parking is Empty
    # ---------------------------------------------------

    def is_empty(self, zone):
        """
        Returns True if no vehicles are parked.
        """

        if not self.zone_exists(zone):
            return False

        return self.occupancy[zone] == 0

    # ---------------------------------------------------
    # Get All Zone Names
    # ---------------------------------------------------

    def get_zone_names(self):
        """
        Return a sorted list of all parking zone IDs.
        """

        return sorted(self.parking_zones.keys())

    # ---------------------------------------------------
    # Get Current Occupancy Snapshot
    # ---------------------------------------------------

    def occupancy_snapshot(self):
        """
        Returns current occupancy data.
        """

        snapshot = {}

        for zone in self.parking_zones:

            snapshot[zone] = {

                "occupied": self.occupancy[zone],

                "capacity": self.capacity[zone],

                "available": self.available_in_zone(zone)

            }

        return snapshot

    # ---------------------------------------------------
    # Parking Statistics
    # ---------------------------------------------------

    def statistics(self):
        """
        Overall parking statistics.
        """

        utilization = 0

        if self.total_capacity() > 0:

            utilization = round(

                (
                    self.occupied_spaces()
                    /
                    self.total_capacity()
                ) * 100,

                2

            )

        return {

            "zones": len(self.parking_zones),

            "total_capacity": self.total_capacity(),

            "occupied": self.occupied_spaces(),

            "available": self.available_spaces(),

            "utilization": utilization

        }

    # ---------------------------------------------------
    # Print Parking Report
    # ---------------------------------------------------

    def parking_report(self):
        """
        Returns a formatted parking report.
        """

        report = []

        for zone in self.get_zone_names():

            report.append({

                "zone": zone,

                "type": self.parking_zones[zone]["type"],

                "occupied": self.occupancy[zone],

                "capacity": self.capacity[zone],

                "available": self.available_in_zone(zone),

                "gate": self.nearest_gate[zone],

                "price": self.pricing[zone]

            })

        return report