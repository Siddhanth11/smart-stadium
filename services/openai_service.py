# services/openai_service.py

import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class OpenAIService:
    """
    OpenAI Service for Smart Stadium
    """

    def __init__(self):

        self.api_key = os.getenv("OPENAI_API_KEY")

        self.client = None

        if OpenAI and self.api_key:

            self.client = OpenAI(
                api_key=self.api_key
            )

    # ---------------------------------
    # Check Connection
    # ---------------------------------

    def is_connected(self):

        return self.client is not None

    # ---------------------------------
    # Chat Response
    # ---------------------------------

    def chat(self, message):

        if not self.client:

            return {
                "response":
                f"(Demo Mode) You asked: {message}"
            }

        try:

            response = self.client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]

            )

            return {
                "response":
                response.choices[0].message.content
            }

        except Exception as e:

            return {
                "error": str(e)
            }

    # ---------------------------------
    # Match Summary
    # ---------------------------------

    def match_summary(self, score):

        prompt = f"""
        Generate a short football match summary.

        Score:
        {score}
        """

        return self.chat(prompt)

    # ---------------------------------
    # Stadium Chatbot
    # ---------------------------------

    def chatbot(self, question):

        prompt = f"""
        You are a Smart Stadium assistant.

        Answer:

        {question}
        """

        return self.chat(prompt)

    # ---------------------------------
    # Translate Text
    # ---------------------------------

    def translate(
        self,
        text,
        language
    ):

        prompt = f"""

        Translate this text into {language}.

        Text:

        {text}

        """

        return self.chat(prompt)

    # ---------------------------------
    # Emergency Assistant
    # ---------------------------------

    def emergency_help(
        self,
        message
    ):

        prompt = f"""

        Give emergency guidance.

        {message}

        """

        return self.chat(prompt)

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "service": "OpenAI",

            "connected":
                self.is_connected()

        }


# Singleton Object

openai_service = OpenAIService()