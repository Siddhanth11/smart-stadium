# routes/api.py

from flask import Blueprint, jsonify

api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


# -------------------------------------
# API Home
# -------------------------------------

@api_bp.route("/", methods=["GET"])
def home():

    return jsonify({
        "project": "Smart Stadium GenAI",
        "version": "1.0",
        "status": "Running"
    })


# -------------------------------------
# Get All Matches
# -------------------------------------

@api_bp.route("/matches", methods=["GET"])
def get_matches():

    matches = [
        {
            "match_id": 1,
            "team1": "India",
            "team2": "Brazil",
            "date": "15 July 2026"
        },
        {
            "match_id": 2,
            "team1": "Germany",
            "team2": "Argentina",
            "date": "16 July 2026"
        }
    ]

    return jsonify(matches)


# -------------------------------------
# Get All Teams
# -------------------------------------

@api_bp.route("/teams", methods=["GET"])
def get_teams():

    teams = [

        "India",

        "Brazil",

        "Germany",

        "Argentina"

    ]

    return jsonify(teams)


# -------------------------------------
# Get All Players
# -------------------------------------

@api_bp.route("/players", methods=["GET"])
def get_players():

    players = [

        {
            "name": "Player A",
            "team": "India"
        },

        {
            "name": "Player B",
            "team": "Brazil"
        },

        {
            "name": "Player C",
            "team": "Germany"
        }

    ]

    return jsonify(players)


# -------------------------------------
# API Health Check
# -------------------------------------

@api_bp.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "Healthy",
        "service": "Smart Stadium API"
    })
from flask import request


# -------------------------------------
# Book Ticket API
# -------------------------------------

@api_bp.route("/book", methods=["POST"])
def book_ticket():

    data = request.get_json()

    return jsonify({
        "message": "Ticket booked successfully",
        "name": data.get("name"),
        "match_id": data.get("match_id"),
        "seat": data.get("seat")
    })


# -------------------------------------
# Chatbot API
# -------------------------------------

@api_bp.route("/chat", methods=["POST"])
def chatbot():

    data = request.get_json()

    message = data.get("message", "").lower()

    if "ticket" in message:
        reply = "You can book tickets from the Ticket section."

    elif "parking" in message:
        reply = "Parking is available in Zone P1."

    elif "match" in message:
        reply = "Today's match starts at 7:30 PM."

    else:
        reply = "Sorry, I couldn't understand your question."

    return jsonify({
        "question": message,
        "answer": reply
    })


# -------------------------------------
# Navigation API
# -------------------------------------

@api_bp.route("/navigate", methods=["POST"])
def navigate():

    data = request.get_json()

    return jsonify({
        "from": data.get("from"),
        "to": data.get("to"),
        "distance": "250 meters",
        "estimated_time": "4 minutes"
    })


# -------------------------------------
# Emergency API
# -------------------------------------

@api_bp.route("/emergency", methods=["POST"])
def emergency():

    data = request.get_json()

    return jsonify({
        "message": "Emergency alert received.",
        "type": data.get("type"),
        "location": data.get("location"),
        "status": "Active"
    })


# -------------------------------------
# Analytics API
# -------------------------------------

@api_bp.route("/analytics", methods=["GET"])
def analytics():

    return jsonify({
        "attendance": 75000,
        "tickets_sold": 74000,
        "revenue": "₹2,35,70,000"
    })
# -------------------------------------
# Match Summary API
# -------------------------------------

@api_bp.route("/summary", methods=["GET"])
def match_summary():

    return jsonify({
        "match": "India vs Brazil",
        "score": "2 - 1",
        "winner": "India",
        "man_of_the_match": "Player A"
    })


# -------------------------------------
# Parking API
# -------------------------------------

@api_bp.route("/parking", methods=["GET"])
def parking():

    return jsonify({
        "parking_zone": "P1",
        "total_slots": 500,
        "available_slots": 150,
        "status": "Available"
    })


# -------------------------------------
# Seat Recommendation API
# -------------------------------------

@api_bp.route("/seat", methods=["GET"])
def seat_recommendation():

    return jsonify({
        "recommended_seat": "A10",
        "category": "VIP",
        "price": 5000,
        "view": "Excellent"
    })


# -------------------------------------
# Dashboard Summary API
# -------------------------------------

@api_bp.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({
        "matches_today": 2,
        "tickets_sold": 74000,
        "attendance": 75000,
        "crowd_level": "Medium",
        "revenue": "₹2,35,70,000"
    })


# -------------------------------------
# System Status API
# -------------------------------------

@api_bp.route("/status", methods=["GET"])
def system_status():

    return jsonify({
        "system": "Smart Stadium",
        "status": "Running",
        "api_version": "1.0",
        "database": "Connected",
        "ai_services": "Active"
    })