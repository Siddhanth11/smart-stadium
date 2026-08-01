# routes/ticket.py

from flask import Blueprint, jsonify, request

ticket_bp = Blueprint("ticket", __name__, url_prefix="/ticket")


# -------------------------------------
# Home
# -------------------------------------

@ticket_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Smart Stadium Ticket Service"
    })


# -------------------------------------
# View Available Matches
# -------------------------------------

@ticket_bp.route("/matches", methods=["GET"])
def view_matches():

    matches = [
        {
            "match_id": 1,
            "team1": "India",
            "team2": "Brazil",
            "date": "2026-07-15",
            "stadium": "Smart Stadium"
        },
        {
            "match_id": 2,
            "team1": "Germany",
            "team2": "Argentina",
            "date": "2026-07-16",
            "stadium": "Smart Stadium"
        }
    ]

    return jsonify(matches)


# -------------------------------------
# Match Details
# -------------------------------------

@ticket_bp.route("/match/<int:match_id>", methods=["GET"])
def match_details(match_id):

    match = {
        "match_id": match_id,
        "team1": "India",
        "team2": "Brazil",
        "date": "2026-07-15",
        "time": "7:30 PM",
        "stadium": "Smart Stadium",
        "available_seats": 150
    }

    return jsonify(match)


# -------------------------------------
# Book Ticket
# -------------------------------------

@ticket_bp.route("/book", methods=["POST"])
def book_ticket():

    data = request.get_json()

    name = data.get("name")
    match_id = data.get("match_id")
    seat = data.get("seat")

    return jsonify({
        "message": "Ticket booked successfully",
        "name": name,
        "match_id": match_id,
        "seat": seat,
        "status": "Confirmed"
    })


# -------------------------------------
# View Seat Availability
# -------------------------------------

@ticket_bp.route("/seats/<int:match_id>", methods=["GET"])
def seat_availability(match_id):

    seats = {
        "match_id": match_id,
        "available": [
            "A1", "A2", "A3",
            "B1", "B2", "C5"
        ]
    }

    return jsonify(seats)
# -------------------------------------
# Make Payment
# -------------------------------------

@ticket_bp.route("/payment", methods=["POST"])
def payment():

    data = request.get_json()

    amount = data.get("amount")
    method = data.get("method")

    return jsonify({
        "message": "Payment Successful",
        "amount": amount,
        "payment_method": method,
        "status": "Paid"
    })


# -------------------------------------
# Ticket Status
# -------------------------------------

@ticket_bp.route("/status/<ticket_id>", methods=["GET"])
def ticket_status(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "status": "Confirmed",
        "seat": "A10",
        "match": "India vs Brazil"
    })


# -------------------------------------
# QR Ticket
# -------------------------------------

@ticket_bp.route("/qr/<ticket_id>", methods=["GET"])
def qr_ticket(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "qr_code": f"QR-{ticket_id}",
        "message": "Show this QR code at the stadium entrance."
    })


# -------------------------------------
# Download Ticket
# -------------------------------------

@ticket_bp.route("/download/<ticket_id>", methods=["GET"])
def download_ticket(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "file": f"ticket_{ticket_id}.pdf",
        "message": "Ticket ready for download."
    })


# -------------------------------------
# Ticket Price
# -------------------------------------

@ticket_bp.route("/price/<seat>", methods=["GET"])
def ticket_price(seat):

    prices = {
        "VIP": 5000,
        "Premium": 3000,
        "Standard": 1500,
        "Economy": 800
    }

    if seat.upper().startswith("A"):
        category = "VIP"
    elif seat.upper().startswith(("B", "C")):
        category = "Premium"
    elif seat.upper().startswith(("D", "E", "F")):
        category = "Standard"
    else:
        category = "Economy"

    return jsonify({
        "seat": seat,
        "category": category,
        "price": prices[category]
    })
# -------------------------------------
# Cancel Ticket
# -------------------------------------

@ticket_bp.route("/cancel/<ticket_id>", methods=["DELETE"])
def cancel_ticket(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "message": "Ticket cancelled successfully.",
        "status": "Cancelled"
    })


# -------------------------------------
# Ticket History
# -------------------------------------

@ticket_bp.route("/history", methods=["GET"])
def ticket_history():

    history = [
        {
            "ticket_id": "TKT1001",
            "match": "India vs Brazil",
            "seat": "A10",
            "status": "Confirmed"
        },
        {
            "ticket_id": "TKT1002",
            "match": "Germany vs Argentina",
            "seat": "B15",
            "status": "Cancelled"
        }
    ]

    return jsonify(history)


# -------------------------------------
# Validate Ticket
# -------------------------------------

@ticket_bp.route("/validate/<ticket_id>", methods=["GET"])
def validate_ticket(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "valid": True,
        "entry_gate": "Gate A",
        "message": "Ticket is valid."
    })


# -------------------------------------
# Ticket Summary
# -------------------------------------

@ticket_bp.route("/summary/<ticket_id>", methods=["GET"])
def ticket_summary(ticket_id):

    return jsonify({
        "ticket_id": ticket_id,
        "match": "India vs Brazil",
        "stadium": "Smart Stadium",
        "seat": "A10",
        "price": 5000,
        "status": "Confirmed"
    })


# -------------------------------------
# My Tickets
# -------------------------------------

@ticket_bp.route("/mytickets", methods=["GET"])
def my_tickets():

    tickets = [
        {
            "ticket_id": "TKT1001",
            "match": "India vs Brazil",
            "seat": "A10"
        },
        {
            "ticket_id": "TKT1002",
            "match": "Germany vs Argentina",
            "seat": "B15"
        }
    ]

    return jsonify({
        "tickets": tickets
    })