# routes/volunteer.py

from flask import Blueprint, jsonify, request

volunteer_bp = Blueprint(
    "volunteer",
    __name__,
    url_prefix="/volunteer"
)


# -------------------------------------
# Volunteer Home
# -------------------------------------

@volunteer_bp.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Smart Stadium Volunteer Portal"
    })


# -------------------------------------
# Volunteer Login
# -------------------------------------

@volunteer_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    volunteer_id = data.get("volunteer_id")
    password = data.get("password")

    if volunteer_id == "VOL001" and password == "1234":

        return jsonify({
            "message": "Login Successful",
            "volunteer_id": volunteer_id
        })

    return jsonify({
        "message": "Invalid Volunteer ID or Password"
    }), 401


# -------------------------------------
# Volunteer Profile
# -------------------------------------

@volunteer_bp.route("/profile", methods=["GET"])
def profile():

    return jsonify({
        "volunteer_id": "VOL001",
        "name": "Rahul Sharma",
        "department": "Crowd Management",
        "assigned_gate": "Gate A",
        "status": "Available"
    })


# -------------------------------------
# Volunteer Dashboard
# -------------------------------------

@volunteer_bp.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({
        "tasks_completed": 12,
        "active_tasks": 2,
        "emergency_calls": 1,
        "status": "On Duty"
    })


# -------------------------------------
# Assigned Area
# -------------------------------------

@volunteer_bp.route("/area", methods=["GET"])
def assigned_area():

    return jsonify({
        "area": "Gate A",
        "role": "Crowd Control",
        "shift": "09:00 AM - 05:00 PM"
    })
# -------------------------------------
# Assigned Tasks
# -------------------------------------

@volunteer_bp.route("/tasks", methods=["GET"])
def tasks():

    task_list = [
        {
            "task_id": 1,
            "task": "Manage Crowd at Gate A",
            "status": "Pending"
        },
        {
            "task_id": 2,
            "task": "Help Visitors",
            "status": "In Progress"
        }
    ]

    return jsonify(task_list)


# -------------------------------------
# Emergency Response
# -------------------------------------

@volunteer_bp.route("/emergency", methods=["GET"])
def emergency():

    return jsonify({
        "emergency": "Medical Assistance Required",
        "location": "North Stand",
        "priority": "High"
    })


# -------------------------------------
# Update Volunteer Status
# -------------------------------------

@volunteer_bp.route("/status", methods=["POST"])
def update_status():

    data = request.get_json()

    status = data.get("status")

    return jsonify({
        "message": "Status Updated Successfully",
        "current_status": status
    })


# -------------------------------------
# Contact Admin
# -------------------------------------

@volunteer_bp.route("/contact-admin", methods=["GET"])
def contact_admin():

    return jsonify({
        "admin_name": "Stadium Manager",
        "phone": "+91-9876543210",
        "email": "admin@smartstadium.com"
    })


# -------------------------------------
# Report Incident
# -------------------------------------

@volunteer_bp.route("/report", methods=["POST"])
def report_incident():

    data = request.get_json()

    incident = data.get("incident")
    location = data.get("location")

    return jsonify({
        "message": "Incident Report Submitted",
        "incident": incident,
        "location": location,
        "status": "Reported"
    })
# -------------------------------------
# Task History
# -------------------------------------

@volunteer_bp.route("/history", methods=["GET"])
def task_history():

    history = [
        {
            "task_id": 101,
            "task": "Crowd Management",
            "status": "Completed"
        },
        {
            "task_id": 102,
            "task": "Emergency Assistance",
            "status": "Completed"
        }
    ]

    return jsonify(history)


# -------------------------------------
# Performance Summary
# -------------------------------------

@volunteer_bp.route("/performance", methods=["GET"])
def performance():

    return jsonify({
        "tasks_completed": 25,
        "emergencies_handled": 5,
        "rating": 4.8,
        "status": "Excellent"
    })


# -------------------------------------
# Shift Details
# -------------------------------------

@volunteer_bp.route("/shift", methods=["GET"])
def shift():

    return jsonify({
        "shift": "Morning",
        "timing": "09:00 AM - 05:00 PM",
        "assigned_gate": "Gate A",
        "supervisor": "Mr. Kumar"
    })


# -------------------------------------
# Notifications
# -------------------------------------

@volunteer_bp.route("/notifications", methods=["GET"])
def notifications():

    notification_list = [
        "Report to Gate A before 9:00 AM.",
        "Medical emergency drill at 2:00 PM.",
        "Team meeting at 5:15 PM."
    ]

    return jsonify({
        "notifications": notification_list
    })


# -------------------------------------
# Logout
# -------------------------------------

@volunteer_bp.route("/logout", methods=["POST"])
def logout():

    return jsonify({
        "message": "Volunteer logged out successfully."
    })