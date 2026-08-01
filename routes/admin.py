from flask import Blueprint, jsonify, request

admin_bp = Blueprint("admin", __name__)

# -------------------------
# Dashboard
# -------------------------

@admin_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify({
        "message": "Welcome Admin",
        "total_users": 120,
        "total_matches": 15,
        "tickets_sold": 850,
        "active_volunteers": 40
    })


# -------------------------
# Users
# -------------------------

users = []


@admin_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@admin_bp.route("/users", methods=["POST"])
def add_user():

    data = request.json

    users.append(data)

    return jsonify({
        "message": "User added successfully",
        "user": data
    })


# -------------------------
# Matches
# -------------------------

matches = []


@admin_bp.route("/matches", methods=["GET"])
def get_matches():
    return jsonify(matches)


@admin_bp.route("/matches", methods=["POST"])
def add_match():

    data = request.json

    matches.append(data)

    return jsonify({
        "message": "Match added successfully",
        "match": data
    })


# -------------------------
# Stadium
# -------------------------

stadium = {
    "name": "Smart Stadium",
    "capacity": 50000,
    "location": "Bengaluru"
}


@admin_bp.route("/stadium", methods=["GET"])
def get_stadium():
    return jsonify(stadium)


# -------------------------
# Volunteers
# -------------------------

volunteers = []


@admin_bp.route("/volunteers", methods=["GET"])
def get_volunteers():
    return jsonify(volunteers)


@admin_bp.route("/volunteers", methods=["POST"])
def add_volunteer():

    data = request.json

    volunteers.append(data)

    return jsonify({
        "message": "Volunteer added",
        "volunteer": data
    })


# -------------------------
# Analytics
# -------------------------

@admin_bp.route("/analytics", methods=["GET"])
def analytics():

    return jsonify({
        "attendance": 42000,
        "parking_usage": "82%",
        "crowd_level": "Medium",
        "revenue": "₹15,00,000"
    })


# -------------------------
# Emergency
# -------------------------

@admin_bp.route("/emergency", methods=["GET"])
def emergency():

    return jsonify({
        "status": "No Active Emergency"
    })