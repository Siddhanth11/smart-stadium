# routes/navigation.py

from flask import Blueprint, jsonify, request

navigation_bp = Blueprint(
    "navigation",
    __name__,
    url_prefix="/navigation"
)


# -------------------------------------
# Navigation Home
# -------------------------------------

@navigation_bp.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Smart Stadium Navigation Service"
    })


# -------------------------------------
# Stadium Map
# -------------------------------------

@navigation_bp.route("/map", methods=["GET"])
def stadium_map():

    return jsonify({
        "stadium": "Smart Stadium",
        "gates": [
            "Gate A",
            "Gate B",
            "Gate C",
            "Gate D"
        ],
        "parking": "Parking Zone P1",
        "medical": "Medical Center",
        "food_court": "Food Court"
    })


# -------------------------------------
# Find Route
# -------------------------------------

@navigation_bp.route("/route", methods=["POST"])
def find_route():

    data = request.get_json()

    start = data.get("start")
    destination = data.get("destination")

    return jsonify({
        "start": start,
        "destination": destination,
        "route": [
            start,
            "Main Corridor",
            destination
        ],
        "distance": "250 meters"
    })


# -------------------------------------
# Nearest Gate
# -------------------------------------

@navigation_bp.route("/gate", methods=["GET"])
def nearest_gate():

    location = request.args.get("location")

    return jsonify({
        "current_location": location,
        "nearest_gate": "Gate A",
        "distance": "120 meters"
    })


# -------------------------------------
# Parking Information
# -------------------------------------

@navigation_bp.route("/parking", methods=["GET"])
def parking():

    return jsonify({
        "parking_zone": "P1",
        "available_slots": 150,
        "status": "Available"
    })
# -------------------------------------
# Seat Navigation
# -------------------------------------

@navigation_bp.route("/seat/<seat_no>", methods=["GET"])
def seat_navigation(seat_no):

    return jsonify({
        "seat": seat_no,
        "route": [
            "Gate A",
            "Main Corridor",
            f"Row {seat_no[0]}",
            seat_no
        ],
        "distance": "180 meters"
    })


# -------------------------------------
# Food Court Navigation
# -------------------------------------

@navigation_bp.route("/foodcourt", methods=["GET"])
def food_court():

    return jsonify({
        "destination": "Food Court",
        "route": [
            "Current Location",
            "Central Hall",
            "Food Court"
        ],
        "distance": "90 meters",
        "time": "2 minutes"
    })


# -------------------------------------
# Washroom Navigation
# -------------------------------------

@navigation_bp.route("/washroom", methods=["GET"])
def washroom():

    return jsonify({
        "nearest_washroom": "Washroom Block B",
        "distance": "60 meters",
        "time": "1 minute"
    })


# -------------------------------------
# Emergency Exit
# -------------------------------------

@navigation_bp.route("/emergency", methods=["GET"])
def emergency_exit():

    return jsonify({
        "nearest_exit": "Emergency Exit A",
        "route": [
            "Current Location",
            "Emergency Corridor",
            "Exit A"
        ],
        "distance": "70 meters"
    })


# -------------------------------------
# Navigation Status
# -------------------------------------

@navigation_bp.route("/status", methods=["GET"])
def navigation_status():

    return jsonify({
        "navigation": "Active",
        "crowd_level": "Medium",
        "recommended_gate": "Gate A"
    })
# -------------------------------------
# Parking Route
# -------------------------------------

@navigation_bp.route("/parking/<zone>", methods=["GET"])
def parking_route(zone):

    return jsonify({
        "parking_zone": zone.upper(),
        "route": [
            "Current Location",
            "Parking Road",
            f"Parking {zone.upper()}"
        ],
        "distance": "220 meters",
        "time": "4 minutes"
    })


# -------------------------------------
# AI Route Suggestion
# -------------------------------------

@navigation_bp.route("/best-route", methods=["GET"])
def best_route():

    destination = request.args.get("destination", "Main Gate")

    return jsonify({
        "destination": destination,
        "recommended_route": [
            "Current Location",
            "Central Corridor",
            destination
        ],
        "estimated_time": "3 minutes",
        "crowd_level": "Low"
    })


# -------------------------------------
# Nearby Places
# -------------------------------------

@navigation_bp.route("/nearby", methods=["GET"])
def nearby_places():

    return jsonify({
        "places": [
            "Food Court",
            "Medical Center",
            "Restroom",
            "Parking P1",
            "Fan Zone"
        ]
    })


# -------------------------------------
# Navigation Summary
# -------------------------------------

@navigation_bp.route("/summary", methods=["GET"])
def navigation_summary():

    return jsonify({
        "stadium": "Smart Stadium",
        "total_gates": 4,
        "parking_zones": 3,
        "food_courts": 2,
        "medical_centers": 2,
        "status": "Navigation Service Running"
    })


# -------------------------------------
# Navigation History
# -------------------------------------

@navigation_bp.route("/history", methods=["GET"])
def navigation_history():

    history = [
        {
            "from": "Gate A",
            "to": "Seat A10"
        },
        {
            "from": "Seat A10",
            "to": "Food Court"
        }
    ]

    return jsonify({
        "history": history
    })