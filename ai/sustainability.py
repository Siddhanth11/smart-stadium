# ai/sustainability.py

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class SustainabilityAI:
    """
    Smart Stadium Sustainability AI
    Monitors energy, water, waste and environmental metrics.
    """

    def __init__(self):

        logging.info(
            "Initializing Sustainability AI..."
        )

        # ---------------------------------
        # Energy Statistics (kWh)
        # ---------------------------------

        self.energy = {

            "consumed": 0,

            "saved": 0

        }

        # ---------------------------------
        # Water Statistics (Litres)
        # ---------------------------------

        self.water = {

            "consumed": 0,

            "saved": 0

        }

        # ---------------------------------
        # Waste Statistics (Kg)
        # ---------------------------------

        self.waste = {

            "generated": 0,

            "recycled": 0

        }

        # ---------------------------------
        # Carbon Emission (Kg CO₂)
        # ---------------------------------

        self.carbon = {

            "produced": 0,

            "reduced": 0

        }

        # ---------------------------------
        # AI History
        # ---------------------------------

        self.history = []

        logging.info(
            "Sustainability AI Ready."
        )

    # ---------------------------------
    # Current Time
    # ---------------------------------

    def current_time(self):

        return datetime.now()

    # ---------------------------------
    # Update Energy
    # ---------------------------------

    def update_energy(
        self,
        consumed,
        saved=0
    ):

        self.energy["consumed"] = consumed
        self.energy["saved"] = saved

    # ---------------------------------
    # Update Water
    # ---------------------------------

    def update_water(
        self,
        consumed,
        saved=0
    ):

        self.water["consumed"] = consumed
        self.water["saved"] = saved

    # ---------------------------------
    # Update Waste
    # ---------------------------------

    def update_waste(
        self,
        generated,
        recycled
    ):

        self.waste["generated"] = generated
        self.waste["recycled"] = recycled

    # ---------------------------------
    # Update Carbon
    # ---------------------------------

    def update_carbon(
        self,
        produced,
        reduced=0
    ):

        self.carbon["produced"] = produced
        self.carbon["reduced"] = reduced

    # ---------------------------------
    # Total Energy Saved
    # ---------------------------------

    def energy_saved(self):

        return self.energy["saved"]

    # ---------------------------------
    # Total Water Saved
    # ---------------------------------

    def water_saved(self):

        return self.water["saved"]

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "status": "Healthy",

            "records":
                len(self.history)

        }

    # ---------------------------------
    # Statistics
    # ---------------------------------

    def statistics(self):

        return {

            "energy":
                self.energy,

            "water":
                self.water,

            "waste":
                self.waste,

            "carbon":
                self.carbon

        }

    # ---------------------------------
    # Reset History
    # ---------------------------------

    def reset_history(self):

        self.history.clear()

        logging.info(
            "History reset successfully."
        )

    # ---------------------------------
    # Summary
    # ---------------------------------

    def summary(self):

        return {

            "health":
                self.health(),

            "statistics":
                self.statistics()

        }
    # ---------------------------------
    # Energy Efficiency
    # ---------------------------------

    def energy_efficiency(self):

        consumed = self.energy["consumed"]
        saved = self.energy["saved"]

        if consumed == 0:
            return 0

        return round((saved / consumed) * 100, 2)

    # ---------------------------------
    # Water Efficiency
    # ---------------------------------

    def water_efficiency(self):

        consumed = self.water["consumed"]
        saved = self.water["saved"]

        if consumed == 0:
            return 0

        return round((saved / consumed) * 100, 2)

    # ---------------------------------
    # Recycling Percentage
    # ---------------------------------

    def recycling_rate(self):

        generated = self.waste["generated"]
        recycled = self.waste["recycled"]

        if generated == 0:
            return 0

        return round((recycled / generated) * 100, 2)

    # ---------------------------------
    # Carbon Reduction
    # ---------------------------------

    def carbon_reduction(self):

        produced = self.carbon["produced"]
        reduced = self.carbon["reduced"]

        if produced == 0:
            return 0

        return round((reduced / produced) * 100, 2)

    # ---------------------------------
    # Green Score
    # ---------------------------------

    def green_score(self):

        score = (

            self.energy_efficiency()

            + self.water_efficiency()

            + self.recycling_rate()

            + self.carbon_reduction()

        ) / 4

        return round(score, 2)

    # ---------------------------------
    # Sustainability Grade
    # ---------------------------------

    def sustainability_grade(self):

        score = self.green_score()

        if score >= 90:
            return "A+"

        elif score >= 80:
            return "A"

        elif score >= 70:
            return "B"

        elif score >= 60:
            return "C"

        return "Needs Improvement"

    # ---------------------------------
    # Carbon Footprint
    # ---------------------------------

    def carbon_footprint(self):

        return {

            "produced":
                self.carbon["produced"],

            "reduced":
                self.carbon["reduced"],

            "reduction_percentage":
                self.carbon_reduction()

        }

    # ---------------------------------
    # Sustainability Dashboard
    # ---------------------------------

    def dashboard(self):

        return {

            "energy_efficiency":
                self.energy_efficiency(),

            "water_efficiency":
                self.water_efficiency(),

            "recycling_rate":
                self.recycling_rate(),

            "carbon_reduction":
                self.carbon_reduction(),

            "green_score":
                self.green_score(),

            "grade":
                self.sustainability_grade()

        }
    # ---------------------------------
    # Save Current Record
    # ---------------------------------

    def save_record(self):

        record = {

            "time":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "energy":
                self.energy.copy(),

            "water":
                self.water.copy(),

            "waste":
                self.waste.copy(),

            "carbon":
                self.carbon.copy(),

            "green_score":
                self.green_score(),

            "grade":
                self.sustainability_grade()

        }

        self.history.append(record)

        return record

    # ---------------------------------
    # AI Recommendation
    # ---------------------------------

    def recommendation(self):

        score = self.green_score()

        if score >= 90:

            return "Excellent sustainability performance."

        elif score >= 75:

            return "Good performance. Continue current practices."

        elif score >= 60:

            return "Improve recycling and energy saving."

        else:

            return (
                "Increase renewable energy usage, "
                "reduce water consumption, and improve recycling."
            )

    # ---------------------------------
    # Sustainability Analytics
    # ---------------------------------

    def analytics(self):

        return {

            "records":
                len(self.history),

            "latest_score":
                self.green_score(),

            "grade":
                self.sustainability_grade(),

            "recommendation":
                self.recommendation()

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

            "dashboard":
                self.dashboard(),

            "analytics":
                self.analytics(),

            "history":
                self.history

        }

    # ---------------------------------
    # AI Insights
    # ---------------------------------

    def insights(self):

        return [

            f"Energy Efficiency : {self.energy_efficiency()}%",

            f"Water Efficiency : {self.water_efficiency()}%",

            f"Recycling Rate : {self.recycling_rate()}%",

            f"Carbon Reduction : {self.carbon_reduction()}%",

            f"Green Score : {self.green_score()}",

            f"Grade : {self.sustainability_grade()}"

        ]

    # ---------------------------------
    # Complete Summary
    # ---------------------------------

    def complete_summary(self):

        return {

            "health":
                self.health(),

            "dashboard":
                self.dashboard(),

            "analytics":
                self.analytics(),

            "insights":
                self.insights()

        }

    # ---------------------------------
    # Reset Module
    # ---------------------------------

    def reset(self):

        self.energy = {
            "consumed": 0,
            "saved": 0
        }

        self.water = {
            "consumed": 0,
            "saved": 0
        }

        self.waste = {
            "generated": 0,
            "recycled": 0
        }

        self.carbon = {
            "produced": 0,
            "reduced": 0
        }

        self.history.clear()

        logging.info(
            "Sustainability AI reset."
        )

        return {

            "success": True,

            "message":
                "All sustainability records cleared."

        }