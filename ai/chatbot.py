"""
AI Chatbot Module
Smart Stadium GenAI
"""

import os
import logging
from datetime import datetime

from config import Config
from services.openai_service import OpenAIService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class ChatbotAI:
    """
    Stadium AI Chatbot
    """

    def __init__(self):

        self.openai = OpenAIService()

        self.model = getattr(
            Config,
            "OPENAI_MODEL",
            "gpt-4o-mini"
        )

        self.max_history = 10

        self.history = []

        self.system_prompt = """
You are Smart Stadium AI Assistant.

Your job is to help fans inside the stadium.

You answer questions about:

• Stadium navigation
• Ticket information
• Seat recommendations
• Parking
• Match schedule
• Team information
• Emergency exits
• Washrooms
• Food courts
• Medical rooms
• Weather
• Live match updates
• Accessibility services
• Lost and Found

Always answer politely.

If you don't know the answer,
reply politely instead of guessing.
"""

        logging.info("Smart Stadium Chatbot Initialized")

    # --------------------------

    def clear_history(self):
        """
        Remove all conversation history.
        """

        self.history = []

    # --------------------------

    def add_message(
        self,
        role,
        message
    ):

        self.history.append({

            "role": role,

            "content": message

        })

        if len(self.history) > self.max_history:

            self.history = self.history[-self.max_history:]

    # --------------------------

    def get_history(self):

        return self.history

    # --------------------------

    def build_messages(
        self,
        user_message
    ):

        messages = [

            {
                "role": "system",
                "content": self.system_prompt
            }

        ]

        messages.extend(self.history)

        messages.append({

            "role": "user",

            "content": user_message

        })

        return messages
    # --------------------------

    def fallback_response(self, user_message: str) -> str:
        """
        Returns a fallback response when the AI service
        is unavailable or an error occurs.
        """

        message = user_message.lower()

        if "ticket" in message:
            return (
                "You can book or view your tickets from the Tickets "
                "section of the Smart Stadium dashboard."
            )

        if "parking" in message:
            return (
                "Parking is available near Gates A, B and C. "
                "Please follow the parking signs."
            )

        if "food" in message:
            return (
                "Food courts are located on Level 1 and Level 2."
            )

        if "washroom" in message or "toilet" in message:
            return (
                "Washrooms are available near every seating block."
            )

        if "emergency" in message:
            return (
                "Please contact the nearest volunteer or proceed "
                "to the nearest emergency exit."
            )

        if "gate" in message:
            return (
                "Please check your ticket for your assigned gate."
            )

        return (
            "I'm sorry, I couldn't process your request right now. "
            "Please try again in a few moments."
        )

    # --------------------------

    def generate_response(self, user_message: str) -> str:
        """
        Generate an AI response using the OpenAI service.
        """

        try:

            messages = self.build_messages(user_message)

            response = self.openai.chat_completion(
                messages=messages,
                model=self.model,
                temperature=0.4
            )

            if not response:
                raise Exception("Empty AI response.")

            self.add_message(
                "user",
                user_message
            )

            self.add_message(
                "assistant",
                response
            )

            return response

        except Exception as e:

            logging.exception(e)

            return self.fallback_response(user_message)

    # --------------------------

    def ask(self, question: str) -> dict:
        """
        Public method used by Flask routes.
        """

        answer = self.generate_response(question)

        return {

            "success": True,

            "question": question,

            "answer": answer,

            "timestamp": datetime.utcnow().isoformat()

        }

    # --------------------------

    def chat(self, question: str) -> str:
        """
        Returns only the chatbot reply.
        """

        return self.generate_response(question)

    # --------------------------

    def last_messages(self, limit: int = 5):
        """
        Return recent conversation history.
        """

        return self.history[-limit:]
# ---------------------------------------------------
# Greeting Detection
# ---------------------------------------------------

    def is_greeting(self, message):

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        message = message.lower().strip()

        return any(greet in message for greet in greetings)


# ---------------------------------------------------
# Greeting Response
# ---------------------------------------------------

    def greeting_response(self):

        return (
            "👋 Hello! Welcome to Smart Stadium.\n\n"
            "I can help you with:\n"
            "• Stadium Navigation\n"
            "• Match Schedule\n"
            "• Ticket Information\n"
            "• Seat Recommendation\n"
            "• Parking Availability\n"
            "• Food Courts\n"
            "• Washrooms\n"
            "• Emergency Assistance\n"
            "• Live Match Updates\n\n"
            "How may I help you today?"
        )


# ---------------------------------------------------
# Frequently Asked Questions
# ---------------------------------------------------

    def faq_answers(self):

        return {

            "parking":
                "Parking is available near Gates A, B and C.",

            "ticket":
                "Tickets can be booked from the Tickets page.",

            "food":
                "Food courts are available on Level 1 and Level 2.",

            "restaurant":
                "Food courts are located near Gate 2 and Gate 5.",

            "washroom":
                "Washrooms are available in every seating block.",

            "toilet":
                "Nearest washroom information is available on the navigation page.",

            "gate":
                "Please check your ticket for your assigned entry gate.",

            "match":
                "You can view today's match schedule from the Dashboard.",

            "wifi":
                "Free Wi-Fi is available throughout the stadium.",

            "medical":
                "Medical rooms are available near Gate 4.",

            "hospital":
                "Emergency medical staff are available 24×7.",

            "atm":
                "ATM services are available near the main entrance.",

            "lost":
                "Please visit the Lost & Found counter near Gate 1.",

            "exit":
                "Emergency exits are marked throughout the stadium.",

            "volunteer":
                "Volunteers are wearing blue jackets and ID cards."
        }


# ---------------------------------------------------
# Intent Detection
# ---------------------------------------------------

    def detect_intent(self, message):

        message = message.lower()

        intents = {

            "ticket": [
                "ticket",
                "book",
                "booking",
                "seat"
            ],

            "parking": [
                "parking",
                "car",
                "bike"
            ],

            "food": [
                "food",
                "restaurant",
                "snacks"
            ],

            "navigation": [
                "gate",
                "map",
                "navigate",
                "route"
            ],

            "medical": [
                "medical",
                "hospital",
                "doctor"
            ],

            "emergency": [
                "emergency",
                "fire",
                "security"
            ],

            "match": [
                "match",
                "score",
                "live",
                "team"
            ],

            "volunteer": [
                "volunteer",
                "help"
            ]
        }

        for intent, keywords in intents.items():

            for keyword in keywords:

                if keyword in message:

                    return intent

        return "general"


# ---------------------------------------------------
# FAQ Search
# ---------------------------------------------------

    def search_faq(self, message):

        message = message.lower()

        faqs = self.faq_answers()

        for keyword, answer in faqs.items():

            if keyword in message:

                return answer

        return None


# ---------------------------------------------------
# Quick Response
# ---------------------------------------------------

    def quick_reply(self, message):

        if self.is_greeting(message):

            return self.greeting_response()

        faq = self.search_faq(message)

        if faq:

            return faq

        return None