# ai/attendance_prediction.py

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class AttendancePredictionAI:

    def __init__(self):

        logging.info(
            "Initializing Attendance Prediction AI..."
        )

        # Stadium Capacity
        self.capacity = 80000

        # Match Data
        self.matches = {}

        # Prediction History
        self.history = []

        # Team Popularity
        self.team_popularity = {

            "India": 95,
            "Brazil": 92,
            "Argentina": 90,
            "Germany": 88,
            "France": 87,
            "Spain": 86

        }

        # Weather Impact
        self.weather_factor = {

            "Sunny": 1.00,
            "Cloudy": 0.95,
            "Rainy": 0.80,
            "Storm": 0.60

        }

        logging.info(
            "Attendance Prediction AI Ready."
        )

    # ---------------------------------
    # Current Time
    # ---------------------------------

    def current_time(self):

        return datetime.now()

    # ---------------------------------
    # Health
    # ---------------------------------

    def health(self):

        return {

            "status": "Healthy",

            "matches": len(self.matches),

            "history": len(self.history)

        }

    # ---------------------------------
    # Add Match
    # ---------------------------------

    def add_match(
        self,
        match_id,
        home,
        away,
        tickets
    ):

        self.matches[match_id] = {

            "home": home,

            "away": away,

            "tickets": tickets

        }

    # ---------------------------------
    # Match Exists
    # ---------------------------------

    def match_exists(self, match_id):

        return match_id in self.matches

    # ---------------------------------
    # Match Details
    # ---------------------------------

    def match_details(self, match_id):

        return self.matches.get(match_id)

    # ---------------------------------
    # Team Popularity
    # ---------------------------------

    def popularity(self, team):

        return self.team_popularity.get(
            team,
            75
        )

    # ---------------------------------
    # Weather Score
    # ---------------------------------

    def weather_score(self, weather):

        return self.weather_factor.get(
            weather,
            1.0
        )

    # ---------------------------------
    # Capacity
    # ---------------------------------

    def stadium_capacity(self):

        return self.capacity

    # ---------------------------------
    # Total Matches
    # ---------------------------------

    def total_matches(self):

        return len(self.matches)

    # ---------------------------------
    # Prediction History
    # ---------------------------------

    def prediction_history(self):

        return self.history

    # ---------------------------------
    # Statistics
    # ---------------------------------

    def statistics(self):

        return {

            "capacity":
                self.capacity,

            "registered_matches":
                self.total_matches(),

            "predictions":
                len(self.history)

        }

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.matches.clear()

        self.history.clear()

        logging.info(
            "Attendance Prediction AI reset."
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
    # Predict Attendance
    # ---------------------------------

    def predict_attendance(
        self,
        match_id,
        weather="Sunny"
    ):

        if not self.match_exists(match_id):

            return {
                "success": False,
                "message": "Match not found."
            }

        match = self.matches[match_id]

        home_score = self.popularity(
            match["home"]
        )

        away_score = self.popularity(
            match["away"]
        )

        popularity_score = (
            home_score + away_score
        ) / 2

        weather_factor = self.weather_score(
            weather
        )

        ticket_sales = match["tickets"]

        predicted = int(
            ticket_sales *
            weather_factor *
            (popularity_score / 100)
        )

        predicted = min(
            predicted,
            self.capacity
        )

        prediction = {

            "match_id": match_id,

            "home_team": match["home"],

            "away_team": match["away"],

            "weather": weather,

            "tickets_sold": ticket_sales,

            "predicted_attendance":
                predicted

        }

        self.history.append(prediction)

        return prediction

    # ---------------------------------
    # Occupancy Percentage
    # ---------------------------------

    def occupancy(
        self,
        attendance
    ):

        return round(
            (attendance / self.capacity) * 100,
            2
        )

    # ---------------------------------
    # Attendance Level
    # ---------------------------------

    def attendance_level(
        self,
        attendance
    ):

        percentage = self.occupancy(
            attendance
        )

        if percentage < 40:
            return "Low"

        elif percentage < 70:
            return "Medium"

        elif percentage < 90:
            return "High"

        return "Full"

    # ---------------------------------
    # Confidence Score
    # ---------------------------------

    def confidence_score(
        self,
        weather
    ):

        scores = {

            "Sunny": 95,

            "Cloudy": 90,

            "Rainy": 75,

            "Storm": 60

        }

        return scores.get(
            weather,
            85
        )

    # ---------------------------------
    # Prediction Report
    # ---------------------------------

    def prediction_report(
        self,
        match_id,
        weather="Sunny"
    ):

        prediction = self.predict_attendance(
            match_id,
            weather
        )

        if not prediction.get("success", True):
            return prediction

        attendance = prediction[
            "predicted_attendance"
        ]

        prediction["occupancy"] = (
            self.occupancy(attendance)
        )

        prediction["attendance_level"] = (
            self.attendance_level(attendance)
        )

        prediction["confidence"] = (
            self.confidence_score(weather)
        )

        return prediction

    # ---------------------------------
    # Prediction Dashboard
    # ---------------------------------

    def dashboard(self):

        return {

            "matches":
                self.total_matches(),

            "predictions":
                len(self.history),

            "capacity":
                self.capacity,

            "history":
                self.history

        }
    # ---------------------------------
    # Average Attendance
    # ---------------------------------

    def average_attendance(self):

        if not self.history:
            return 0

        total = sum(
            item["predicted_attendance"]
            for item in self.history
        )

        return round(
            total / len(self.history),
            2
        )

    # ---------------------------------
    # Highest Prediction
    # ---------------------------------

    def highest_prediction(self):

        if not self.history:
            return None

        return max(
            self.history,
            key=lambda x: x["predicted_attendance"]
        )

    # ---------------------------------
    # Lowest Prediction
    # ---------------------------------

    def lowest_prediction(self):

        if not self.history:
            return None

        return min(
            self.history,
            key=lambda x: x["predicted_attendance"]
        )

    # ---------------------------------
    # AI Recommendation
    # ---------------------------------

    def recommendation(self, attendance):

        level = self.attendance_level(attendance)

        if level == "Low":
            return "Increase promotions to boost attendance."

        elif level == "Medium":
            return "Maintain regular stadium operations."

        elif level == "High":
            return "Deploy additional security and volunteers."

        return "Prepare full stadium operations."

    # ---------------------------------
    # Prediction Analytics
    # ---------------------------------

    def analytics(self):

        return {

            "average_attendance":
                self.average_attendance(),

            "highest_prediction":
                self.highest_prediction(),

            "lowest_prediction":
                self.lowest_prediction(),

            "total_predictions":
                len(self.history)

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

            "predictions":
                self.history

        }

    # ---------------------------------
    # AI Insights
    # ---------------------------------

    def insights(self):

        insights = []

        if self.history:

            avg = self.average_attendance()

            insights.append(
                f"Average predicted attendance: {avg}"
            )

            highest = self.highest_prediction()

            insights.append(
                f"Highest predicted attendance: "
                f"{highest['predicted_attendance']}"
            )

        else:

            insights.append(
                "No prediction history available."
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