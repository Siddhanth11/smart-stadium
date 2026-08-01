# routes/fan.py

from flask import Blueprint, jsonify, request

fan_bp = Blueprint("fan", __name__, url_prefix="/fan")


# Home
@fan_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Smart Stadium Fan Portal"
    })


# View Matches
@fan_bp.route("/matches", methods=["GET"])
def matches():

    match_list = [
        {
            "id": 1,
            "team1": "India",
            "team2": "Brazil",
            "date": "2026-07-15"
        },
        {
            "id": 2,
            "team1": "Germany",
            "team2": "Argentina",
            "date": "2026-07-16"
        }
    ]

    return jsonify(match_list)


# Match Details
@fan_bp.route("/match/<int:match_id>", methods=["GET"])
def match_details(match_id):

    return jsonify({
        "match_id": match_id,
        "team1": "India",
        "team2": "Brazil",
        "stadium": "Smart Stadium",
        "time": "7:30 PM"
    })


# Stadium Information
@fan_bp.route("/stadium", methods=["GET"])
def stadium():

    return jsonify({
        "name": "Smart Stadium",
        "capacity": 80000,
        "location": "Bengaluru"
    })


# Fan Profile
@fan_bp.route("/profile", methods=["GET"])
def profile():

    return jsonify({
        "name": "Guest Fan",
        "email": "fan@example.com",
        "favorite_team": "India"
    })


# Update Favorite Team
@fan_bp.route("/favorite", methods=["POST"])
def favorite():

    data = request.get_json()

    team = data.get("team")

    return jsonify({
        "message": "Favorite team updated",
        "favorite_team": team
    })


# Notifications
@fan_bp.route("/notifications", methods=["GET"])
def notifications():

    return jsonify([
        "Match starts in 2 hours",
        "Parking is available",
        "Gate A is open"
    ])


# Search
@fan_bp.route("/search", methods=["GET"])
def search():

    keyword = request.args.get("q", "")

    return jsonify({
        "search": keyword,
        "result": f"No result found for '{keyword}'"
    })