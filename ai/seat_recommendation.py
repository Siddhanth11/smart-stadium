"""
Smart Stadium GenAI
Seat Recommendation AI
"""

import logging
import random
import os
import pickle
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class SeatRecommendationAI:
    """
    AI-based Stadium Seat Recommendation System
    """

    def __init__(self):

        logging.info("Initializing Seat Recommendation AI...")

        # -----------------------------
        # Seat Inventory
        # -----------------------------

        self.seats = {}

        # Seat Categories
        self.categories = {}

        # Seat Prices
        self.prices = {}

        # Seat Availability
        self.availability = {}

        # Accessibility Seats
        self.accessible_seats = set()

        # Family Seating
        self.family_seats = set()

        # VIP Seats
        self.vip_seats = set()

        # Premium Seats
        self.premium_seats = set()

        # Economy Seats
        self.economy_seats = set()

        # Stadium Blocks
        self.blocks = []

        # Seat Statistics
        self.statistics = {}

        # User Preferences
        self.preferences = {}

        # Placeholder methods
        self.load_configuration()
        self.load_seats()

        logging.info("Seat Recommendation AI Ready")

    # -------------------------------------
    # Placeholder Methods
    # -------------------------------------

    def load_configuration(self):
        """
        Will be implemented in Part 1A-2.
        """
        pass

    def load_seats(self):
        """
        Will be implemented in Section 2.
        """
        pass

    # -------------------------------------
    # Helper
    # -------------------------------------

    def current_time(self):
        """
        Return current system time.
        """
        return datetime.now()

    # -------------------------------------

    def total_seats(self):
        """
        Total number of seats.
        """
        return len(self.seats)

    # -------------------------------------

    def available_seats(self):
        """
        Count available seats.
        """
        return sum(
            1
            for seat in self.availability
            if self.availability[seat]
        )

    # -------------------------------------

    def occupied_seats(self):
        """
        Count occupied seats.
        """
        return self.total_seats() - self.available_seats()

    # -------------------------------------

    def summary(self):

        return {

            "total_seats": self.total_seats(),

            "available": self.available_seats(),

            "occupied": self.occupied_seats(),

            "blocks": len(self.blocks)

        }
    # -------------------------------------
    # Configuration
    # -------------------------------------

    def load_configuration(self):
        """
        Load AI configuration, pricing,
        preferences and ML model.
        """

        # Seat Categories

        self.categories = {

            "VIP": {
                "description": "Best view with premium services"
            },

            "Premium": {
                "description": "Excellent view"
            },

            "Standard": {
                "description": "Balanced price and visibility"
            },

            "Economy": {
                "description": "Budget friendly seating"
            }

        }

        # Ticket Prices

        self.prices = {

            "VIP": 5000,

            "Premium": 3000,

            "Standard": 1500,

            "Economy": 800

        }

        # Recommendation Preference Weights

        self.preferences = {

            "view": 0.35,

            "price": 0.25,

            "distance": 0.20,

            "availability": 0.20

        }

        # Recommendation Settings

        self.statistics = {

            "recommendations": 0,

            "bookings": 0,

            "last_updated": datetime.now()

        }

        # ML Model

        self.model = None

        model_path = os.path.join(
            "ml_models",
            "seat_model.pkl"
        )

        if os.path.exists(model_path):

            try:

                with open(model_path, "rb") as file:

                    self.model = pickle.load(file)

                logging.info(
                    "Seat recommendation model loaded."
                )

            except Exception as error:

                logging.warning(
                    "Unable to load seat model: %s",
                    error
                )

        else:

            logging.info(
                "seat_model.pkl not found. "
                "Using rule-based recommendation."
            )
    # -------------------------------------

    def get_price(self, category):

        return self.prices.get(category, 0)

    # -------------------------------------

    def category_exists(self, category):

        return category in self.categories

    # -------------------------------------

    def get_categories(self):

        return list(self.categories.keys())

    # -------------------------------------

    def configuration(self):

        return {

            "categories": self.categories,

            "prices": self.prices,

            "preferences": self.preferences,

            "ml_loaded": self.model is not None

        }
    # -------------------------------------
    # Seat Exists
    # -------------------------------------

    def seat_exists(self, seat_id):
        """
        Check whether a seat exists.
        """
        return seat_id in self.seats

    # -------------------------------------

    def is_available(self, seat_id):
        """
        Returns True if the seat is available.
        """
        if not self.seat_exists(seat_id):
            return False

        return self.availability.get(seat_id, False)

    # -------------------------------------

    def get_seat(self, seat_id):
        """
        Return seat information.
        """
        return self.seats.get(seat_id)

    # -------------------------------------

    def get_category(self, seat_id):
        """
        Return seat category.
        """
        if not self.seat_exists(seat_id):
            return None

        return self.seats[seat_id]["category"]

    # -------------------------------------

    def get_block(self, seat_id):
        """
        Return seating block.
        """
        if not self.seat_exists(seat_id):
            return None

        return self.seats[seat_id]["block"]

    # -------------------------------------

    def get_available_by_category(self, category):
        """
        Return all available seats in a category.
        """
        seats = []

        for seat_id, info in self.seats.items():

            if (
                info["category"] == category
                and self.is_available(seat_id)
            ):
                seats.append(seat_id)

        return seats

    # -------------------------------------

    def get_available_by_block(self, block):
        """
        Return all available seats in a block.
        """
        seats = []

        for seat_id, info in self.seats.items():

            if (
                info["block"] == block
                and self.is_available(seat_id)
            ):
                seats.append(seat_id)

        return seats

    # -------------------------------------

    def statistics_report(self):
        """
        Overall seat statistics.
        """

        report = {
            "total": self.total_seats(),
            "available": self.available_seats(),
            "occupied": self.occupied_seats(),
            "categories": {},
            "blocks": len(self.blocks)
        }

        for category in self.categories:

            report["categories"][category] = len(
                self.get_available_by_category(category)
            )

        return report

    # -------------------------------------

    def seat_information(self, seat_id):
        """
        Detailed information for one seat.
        """

        if not self.seat_exists(seat_id):
            return None

        info = self.seats[seat_id]

        return {
            "seat_id": seat_id,
            "block": info["block"],
            "row": info["row"],
            "number": info["number"],
            "category": info["category"],
            "price": self.get_price(info["category"]),
            "available": self.is_available(seat_id),
            "accessible": seat_id in self.accessible_seats,
            "family": seat_id in self.family_seats,
            "vip": seat_id in self.vip_seats
        }

    # -------------------------------------

    def validate_preferences(self, preferences):
        """
        Validate user preference dictionary.
        """

        allowed = {
            "category",
            "max_price",
            "accessible",
            "family",
            "block"
        }

        return all(
            key in allowed
            for key in preferences.keys()
        )
def load_seats(self):
    """
    Generate seats for Stadium Blocks A–F.

    Remaining blocks (G–L) will be added in Part 2A-2.
    """

    # ---------------------------------------------
    # Blocks A–F
    # ---------------------------------------------

    blocks = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F"
    ]

    rows = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J"
    ]

    seats_per_row = 20

    for block in blocks:

        self.blocks.append(block)

        for row in rows:

            for number in range(1, seats_per_row + 1):

                seat_id = f"{block}-{row}{number:02d}"

                self.seats[seat_id] = {

                    "seat_id": seat_id,

                    "block": block,

                    "row": row,

                    "number": number,

                    # Default category
                    # Updated in Part 2B
                    "category": "Standard",

                    # Updated later
                    "view_score": 0,

                    "distance_score": 0,

                    "reserved": False

                }

                self.availability[seat_id] = True

    logging.info(
        "Generated %d seats for Blocks A-F.",
        len(self.seats)
    )
    # ---------------------------------------------
    # Blocks G–L
    # ---------------------------------------------

    additional_blocks = [
        "G",
        "H",
        "I",
        "J",
        "K",
        "L"
    ]

    for block in additional_blocks:

        self.blocks.append(block)

        for row in rows:

            for number in range(1, seats_per_row + 1):

                seat_id = f"{block}-{row}{number:02d}"

                self.seats[seat_id] = {

                    "seat_id": seat_id,

                    "block": block,

                    "row": row,

                    "number": number,

                    # Default values
                    # Updated in Part 2B
                    "category": "Standard",

                    "view_score": 0,

                    "distance_score": 0,

                    "reserved": False

                }

                self.availability[seat_id] = True

    logging.info(
        "Generated %d total seats for Blocks A-L.",
        len(self.seats)
    )
    # ---------------------------------------------
    # Assign Seat Categories
    # ---------------------------------------------

    vip_blocks = {"A", "B"}
    premium_blocks = {"C", "D", "E"}
    standard_blocks = {"F", "G", "H", "I"}
    economy_blocks = {"J", "K", "L"}

    for seat_id, seat in self.seats.items():

        block = seat["block"]

        if block in vip_blocks:
            category = "VIP"
            self.vip_seats.add(seat_id)

        elif block in premium_blocks:
            category = "Premium"
            self.premium_seats.add(seat_id)

        elif block in standard_blocks:
            category = "Standard"

        else:
            category = "Economy"
            self.economy_seats.add(seat_id)

        seat["category"] = category
    # ---------------------------------------------
    # Accessibility, Family & Seat Scores
    # ---------------------------------------------

    for seat_id, seat in self.seats.items():

        row = seat["row"]
        number = seat["number"]
        category = seat["category"]

        # -----------------------------------------
        # Accessibility Seats
        # First row, aisle seats
        # -----------------------------------------

        if row == "A" and number in (1, 2, 19, 20):

            self.accessible_seats.add(seat_id)

        # -----------------------------------------
        # Family Seating
        # Middle rows
        # -----------------------------------------

        if row in ("E", "F"):

            self.family_seats.add(seat_id)

        # -----------------------------------------
        # View Score
        # Higher is better
        # -----------------------------------------

        if category == "VIP":
            seat["view_score"] = 10

        elif category == "Premium":
            seat["view_score"] = 8

        elif category == "Standard":
            seat["view_score"] = 6

        else:
            seat["view_score"] = 4

        # -----------------------------------------
        # Distance Score
        # Higher is closer to ideal viewing area
        # -----------------------------------------

        center_distance = abs(number - 10.5)

        score = max(
            1,
            round(10 - (center_distance / 2))
        )

        seat["distance_score"] = score

    logging.info(
        "Seat metadata initialized for %d seats.",
        len(self.seats)
    )
    # -------------------------------------
    # Validate Seat Inventory
    # -------------------------------------

    def validate_inventory(self):
        """
        Validate the generated seat inventory.
        """

        errors = []

        for seat_id, seat in self.seats.items():

            required = [
                "seat_id",
                "block",
                "row",
                "number",
                "category",
                "view_score",
                "distance_score",
                "reserved"
            ]

            for field in required:

                if field not in seat:
                    errors.append(
                        f"{seat_id}: Missing '{field}'"
                    )

            if seat["category"] not in self.categories:
                errors.append(
                    f"{seat_id}: Invalid category"
                )

            if seat_id not in self.availability:
                errors.append(
                    f"{seat_id}: Availability missing"
                )

        return {

            "valid": len(errors) == 0,

            "errors": errors

        }

    # -------------------------------------
    # Category Statistics
    # -------------------------------------

    def category_statistics(self):

        stats = {}

        for category in self.categories:

            total = 0
            available = 0

            for seat_id, seat in self.seats.items():

                if seat["category"] == category:

                    total += 1

                    if self.availability.get(seat_id):

                        available += 1

            stats[category] = {

                "total": total,

                "available": available,

                "occupied": total - available

            }

        return stats

    # -------------------------------------
    # Block Statistics
    # -------------------------------------

    def block_statistics(self):

        stats = {}

        for block in self.blocks:

            total = 0
            available = 0

            for seat_id, seat in self.seats.items():

                if seat["block"] == block:

                    total += 1

                    if self.availability.get(seat_id):

                        available += 1

            stats[block] = {

                "total": total,

                "available": available,

                "occupied": total - available

            }

        return stats

    # -------------------------------------
    # Accessibility Statistics
    # -------------------------------------

    def accessibility_statistics(self):

        available = sum(
            1
            for seat in self.accessible_seats
            if self.availability.get(seat)
        )

        return {

            "total": len(self.accessible_seats),

            "available": available,

            "occupied":
                len(self.accessible_seats) - available

        }

    # -------------------------------------
    # Family Seating Statistics
    # -------------------------------------

    def family_statistics(self):

        available = sum(
            1
            for seat in self.family_seats
            if self.availability.get(seat)
        )

        return {

            "total": len(self.family_seats),

            "available": available,

            "occupied":
                len(self.family_seats) - available

        }

    # -------------------------------------
    # Overall Seat Statistics
    # -------------------------------------

    def update_statistics(self):

        self.statistics = {

            "generated_at": datetime.now(),

            "total_seats": self.total_seats(),

            "available": self.available_seats(),

            "occupied": self.occupied_seats(),

            "categories": self.category_statistics(),

            "blocks": self.block_statistics(),

            "accessible": self.accessibility_statistics(),

            "family": self.family_statistics()

        }

        return self.statistics
    # -------------------------------------
    # Seat Inventory Report
    # -------------------------------------

    def inventory_report(self):
        """
        Generate a complete inventory report.
        """

        return {

            "summary": self.summary(),

            "statistics": self.statistics,

            "categories": self.category_statistics(),

            "blocks": self.block_statistics(),

            "accessible": self.accessibility_statistics(),

            "family": self.family_statistics()

        }

    # -------------------------------------
    # Export Seats
    # -------------------------------------

    def export_seats(self):

        return list(self.seats.values())

    # -------------------------------------
    # Find Seats in Block
    # -------------------------------------

    def seats_in_block(self, block):

        return [

            seat

            for seat in self.seats.values()

            if seat["block"] == block

        ]

    # -------------------------------------
    # Find Seats by Category
    # -------------------------------------

    def seats_by_category(self, category):

        return [

            seat

            for seat in self.seats.values()

            if seat["category"] == category

        ]

    # -------------------------------------
    # Count Reserved Seats
    # -------------------------------------

    def reserved_count(self):

        return sum(

            1

            for seat in self.seats.values()

            if seat["reserved"]

        )

    # -------------------------------------
    # Count Free Seats
    # -------------------------------------

    def free_count(self):

        return self.total_seats() - self.reserved_count()

    # -------------------------------------
    # Refresh Statistics
    # -------------------------------------

    def refresh(self):

        self.update_statistics()

        return self.statistics

    # -------------------------------------
    # Health Check
    # -------------------------------------

    def health(self):

        validation = self.validate_inventory()

        return {

            "status":
                "Healthy"
                if validation["valid"]
                else "Warning",

            "seat_count":
                self.total_seats(),

            "available":
                self.available_seats(),

            "reserved":
                self.reserved_count(),

            "validation_errors":
                len(validation["errors"])

        }

    # -------------------------------------
    # Initialization Complete
    # -------------------------------------

    def initialize(self):
        """
        Final initialization helper.
        """

        validation = self.validate_inventory()

        if validation["valid"]:

            self.update_statistics()

            logging.info(
                "Seat Recommendation AI initialized successfully."
            )

        else:

            logging.warning(
                "Initialization completed with %d validation errors.",
                len(validation["errors"])
            )

        return validation
# -------------------------------------
# Score a Seat
# -------------------------------------

def score_seat(self, seat_id, preferences=None):
    """
    Calculate a recommendation score for a seat.
    """

    if preferences is None:
        preferences = {}

    if not self.seat_exists(seat_id):
        return -1

    if not self.is_available(seat_id):
        return -1

    seat = self.seats[seat_id]

    score = 0.0

    # -----------------------------
    # View Quality
    # -----------------------------

    score += (
        seat["view_score"]
        * self.preferences["view"]
    )

    # -----------------------------
    # Distance
    # -----------------------------

    score += (
        seat["distance_score"]
        * self.preferences["distance"]
    )

    # -----------------------------
    # Availability Bonus
    # -----------------------------

    score += (
        10
        * self.preferences["availability"]
    )

    # -----------------------------
    # Category Preference
    # -----------------------------

    preferred_category = preferences.get("category")

    if preferred_category:

        if seat["category"] == preferred_category:
            score += 5

        else:
            score -= 2

    # -----------------------------
    # Budget Preference
    # -----------------------------

    max_price = preferences.get("max_price")

    if max_price is not None:

        price = self.get_price(
            seat["category"]
        )

        if price <= max_price:
            score += 3
        else:
            score -= 100

    # -----------------------------
    # Accessible Seating
    # -----------------------------

    if preferences.get("accessible", False):

        if seat_id in self.accessible_seats:
            score += 5
        else:
            score -= 50

    # -----------------------------
    # Family Seating
    # -----------------------------

    if preferences.get("family", False):

        if seat_id in self.family_seats:
            score += 4

    return round(score, 2)


# -------------------------------------
# ML Prediction (Optional)
# -------------------------------------

def ml_score(self, seat_id):
    """
    Predict seat quality using the ML model.
    Returns None if no model is loaded.
    """

    if self.model is None:
        return None

    seat = self.seats[seat_id]

    features = [[
        seat["view_score"],
        seat["distance_score"],
        self.get_price(
            seat["category"]
        )
    ]]

    try:

        prediction = self.model.predict(
            features
        )

        return float(prediction[0])

    except Exception:

        return None


# -------------------------------------
# Recommend Seats
# -------------------------------------

def recommend(self,
              preferences=None,
              limit=5):
    """
    Return the best matching seats.
    """

    if preferences is None:
        preferences = {}

    ranked = []

    for seat_id in self.seats:

        score = self.score_seat(
            seat_id,
            preferences
        )

        if score < 0:
            continue

        ml = self.ml_score(seat_id)

        if ml is not None:
            score = (
                score * 0.7 +
                ml * 0.3
            )

        ranked.append({

            "seat_id": seat_id,

            "score": round(score, 2),

            "category":
                self.get_category(seat_id),

            "price":
                self.get_price(
                    self.get_category(seat_id)
                )

        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    self.statistics["recommendations"] += 1

    return ranked[:limit]

