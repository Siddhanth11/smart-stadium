# routes/analytics.py

from flask import Blueprint, jsonify

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics"
)


# -------------------------------------
# Analytics Home
# -------------------------------------

@analytics_bp.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Smart Stadium Analytics Dashboard"
    })


# -------------------------------------
# Dashboard Overview
# -------------------------------------

@analytics_bp.route("/dashboard", methods=["GET"])
def dashboard():

    data = {
        "total_matches": 12,
        "tickets_sold": 18500,
        "active_fans": 12450,
        "revenue": "₹2,75,00,000"
    }

    return jsonify(data)


# -------------------------------------
# Match Analytics
# -------------------------------------

@analytics_bp.route("/matches", methods=["GET"])
def match_analytics():

    matches = [
        {
            "match": "India vs Brazil",
            "attendance": 75000,
            "tickets_sold": 74000
        },
        {
            "match": "Germany vs Argentina",
            "attendance": 72000,
            "tickets_sold": 71000
        }
    ]

    return jsonify(matches)


# -------------------------------------
# Stadium Overview
# -------------------------------------

@analytics_bp.route("/stadium", methods=["GET"])
def stadium_overview():

    return jsonify({
        "stadium": "Smart Stadium",
        "capacity": 80000,
        "occupied": 75000,
        "available": 5000
    })


# -------------------------------------
# Today's Statistics
# -------------------------------------

@analytics_bp.route("/today", methods=["GET"])
def today():

    return jsonify({
        "matches": 2,
        "tickets": 14500,
        "parking_used": 4200,
        "food_orders": 3100
    })
# -------------------------------------
# Attendance Analytics
# -------------------------------------

@analytics_bp.route("/attendance", methods=["GET"])
def attendance():

    return jsonify({
        "total_attendance": 75000,
        "capacity": 80000,
        "occupancy": "94%"
    })


# -------------------------------------
# Ticket Sales Analytics
# -------------------------------------

@analytics_bp.route("/tickets", methods=["GET"])
def ticket_sales():

    return jsonify({
        "tickets_sold": 74000,
        "tickets_available": 6000,
        "revenue": "₹2,22,00,000"
    })


# -------------------------------------
# Parking Analytics
# -------------------------------------

@analytics_bp.route("/parking", methods=["GET"])
def parking():

    return jsonify({
        "total_slots": 5000,
        "occupied_slots": 4200,
        "available_slots": 800
    })


# -------------------------------------
# Food Court Analytics
# -------------------------------------

@analytics_bp.route("/foodcourt", methods=["GET"])
def foodcourt():

    return jsonify({
        "orders": 3100,
        "revenue": "₹9,50,000",
        "popular_item": "Burger"
    })


# -------------------------------------
# Crowd Analytics
# -------------------------------------

@analytics_bp.route("/crowd", methods=["GET"])
def crowd():

    return jsonify({
        "crowd_level": "Medium",
        "busy_gate": "Gate A",
        "recommended_gate": "Gate C"
    })
# -------------------------------------
# Revenue Analytics
# -------------------------------------

@analytics_bp.route("/revenue", methods=["GET"])
def revenue():

    return jsonify({
        "ticket_revenue": "₹2,22,00,000",
        "food_revenue": "₹9,50,000",
        "parking_revenue": "₹4,20,000",
        "total_revenue": "₹2,35,70,000"
    })


# -------------------------------------
# Match Performance Report
# -------------------------------------

@analytics_bp.route("/report", methods=["GET"])
def report():

    return jsonify({
        "match": "India vs Brazil",
        "attendance": 75000,
        "goals": 3,
        "man_of_the_match": "Player A",
        "result": "India won 2-1"
    })


# -------------------------------------
# Sustainability Report
# -------------------------------------

@analytics_bp.route("/sustainability", methods=["GET"])
def sustainability():

    return jsonify({
        "energy_saved": "1200 kWh",
        "water_saved": "5000 Litres",
        "waste_recycled": "82%",
        "carbon_reduction": "18%"
    })


# -------------------------------------
# AI Insights
# -------------------------------------

@analytics_bp.route("/insights", methods=["GET"])
def insights():

    insights_data = [
        "Gate A has the highest crowd movement.",
        "Food Court sales increased by 12%.",
        "Parking Zone P2 has more availability.",
        "VIP seats achieved 98% occupancy."
    ]

    return jsonify({
        "ai_insights": insights_data
    })


# -------------------------------------
# Analytics Summary
# -------------------------------------

@analytics_bp.route("/summary", methods=["GET"])
def summary():

    return jsonify({
        "matches": 12,
        "attendance": 75000,
        "tickets_sold": 74000,
        "revenue": "₹2,35,70,000",
        "crowd_status": "Medium",
        "system_status": "Healthy"
    })