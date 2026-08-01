# routes/chatbot.py

from flask import Blueprint, jsonify, request

chatbot_bp = Blueprint(
    "chatbot",
    __name__,
    url_prefix="/chatbot"
)


# -------------------------------------
# Chatbot Home
# -------------------------------------

@chatbot_bp.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Smart Stadium AI Chatbot"
    })


# -------------------------------------
# Chat with Bot
# -------------------------------------

@chatbot_bp.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "").lower()

    if "ticket" in message:
        reply = "You can book tickets from the Ticket section."

    elif "match" in message:
        reply = "Today's match starts at 7:30 PM."

    elif "parking" in message:
        reply = "Parking is available in P1 and P2."

    elif "gate" in message:
        reply = "Please enter through Gate A."

    else:
        reply = "Sorry, I don't understand your question."

    return jsonify({
        "user_message": message,
        "bot_reply": reply
    })


# -------------------------------------
# Frequently Asked Questions
# -------------------------------------

@chatbot_bp.route("/faq", methods=["GET"])
def faq():

    questions = [

        {
            "question": "How can I book a ticket?",
            "answer": "Go to the Ticket section and select your match."
        },

        {
            "question": "Where is Parking?",
            "answer": "Parking is available near Gate A and Gate C."
        },

        {
            "question": "Where is the Food Court?",
            "answer": "The Food Court is located near the Central Hall."
        }

    ]

    return jsonify(questions)


# -------------------------------------
# Bot Status
# -------------------------------------

@chatbot_bp.route("/status", methods=["GET"])
def status():

    return jsonify({
        "status": "Online",
        "version": "1.0",
        "service": "Smart Stadium AI Chatbot"
    })


# -------------------------------------
# Help
# -------------------------------------

@chatbot_bp.route("/help", methods=["GET"])
def help():

    return jsonify({
        "commands": [

            "ticket",

            "match",

            "parking",

            "gate",

            "food",

            "seat"

        ]
    })
# -------------------------------------
# Match Information
# -------------------------------------

@chatbot_bp.route("/match", methods=["GET"])
def match_info():

    return jsonify({
        "match": "India vs Brazil",
        "date": "15 July 2026",
        "time": "7:30 PM",
        "stadium": "Smart Stadium"
    })


# -------------------------------------
# Ticket Help
# -------------------------------------

@chatbot_bp.route("/ticket", methods=["GET"])
def ticket_help():

    return jsonify({
        "message": "To book a ticket, go to the Ticket section and choose your preferred match and seat."
    })


# -------------------------------------
# Navigation Help
# -------------------------------------

@chatbot_bp.route("/navigation", methods=["GET"])
def navigation_help():

    return jsonify({
        "message": "Use the Navigation service to find routes to your seat, parking, food court, and exits."
    })


# -------------------------------------
# Language Translation
# -------------------------------------

@chatbot_bp.route("/translate", methods=["POST"])
def translate():

    data = request.get_json()

    text = data.get("text", "")
    language = data.get("language", "English")

    return jsonify({
        "original_text": text,
        "translated_text": text,
        "language": language,
        "message": "Translation service is available."
    })


# -------------------------------------
# Quick Replies
# -------------------------------------

@chatbot_bp.route("/quick-replies", methods=["GET"])
def quick_replies():

    replies = [

        "Book Ticket",

        "Match Schedule",

        "Parking",

        "Seat Navigation",

        "Food Court",

        "Emergency Help"

    ]

    return jsonify({
        "quick_replies": replies
    })
# -------------------------------------
# Emergency Help
# -------------------------------------

@chatbot_bp.route("/emergency", methods=["GET"])
def emergency_help():

    return jsonify({
        "emergency_number": "112",
        "medical_center": "Near Gate B",
        "nearest_exit": "Exit A",
        "message": "Stay calm and follow the emergency instructions."
    })


# -------------------------------------
# AI Match Summary
# -------------------------------------

@chatbot_bp.route("/summary", methods=["GET"])
def match_summary():

    return jsonify({
        "match": "India vs Brazil",
        "score": "2 - 1",
        "summary": "India secured a thrilling victory with a late winning goal."
    })


# -------------------------------------
# Fan Profile Help
# -------------------------------------

@chatbot_bp.route("/profile", methods=["GET"])
def profile_help():

    return jsonify({
        "name": "Guest User",
        "favorite_team": "India",
        "tickets_booked": 2
    })


# -------------------------------------
# Conversation History
# -------------------------------------

@chatbot_bp.route("/history", methods=["GET"])
def chat_history():

    history = [
        {
            "user": "Where is Parking?",
            "bot": "Parking is available in P1."
        },
        {
            "user": "Today's match?",
            "bot": "India vs Brazil at 7:30 PM."
        }
    ]

    return jsonify({
        "history": history
    })


# -------------------------------------
# Feedback
# -------------------------------------

@chatbot_bp.route("/feedback", methods=["POST"])
def feedback():

    data = request.get_json()

    rating = data.get("rating")
    comment = data.get("comment")

    return jsonify({
        "message": "Thank you for your feedback!",
        "rating": rating,
        "comment": comment
    })