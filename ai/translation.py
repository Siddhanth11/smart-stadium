# ai/translation.py

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class TranslationAI:
    """
    AI Translation Module
    """

    def __init__(self):

        logging.info(
            "Initializing Translation AI..."
        )

        # -----------------------------
        # Supported Languages
        # -----------------------------

        self.languages = {

            "en": "English",

            "hi": "Hindi",

            "kn": "Kannada",

            "ta": "Tamil",

            "te": "Telugu",

            "ml": "Malayalam",

            "es": "Spanish",

            "fr": "French",

            "de": "German",

            "pt": "Portuguese"

        }

        # -----------------------------
        # Translation History
        # -----------------------------

        self.history = []

        logging.info(
            "Translation AI Ready."
        )

    # ---------------------------------
    # Current Time
    # ---------------------------------

    def current_time(self):
        """
        Return current date and time.
        """
        return datetime.now()

    # ---------------------------------
    # Supported Languages
    # ---------------------------------

    def supported_languages(self):
        """
        Return all supported languages.
        """
        return self.languages

    # ---------------------------------
    # Language Exists
    # ---------------------------------

    def language_exists(self, code):
        """
        Check if a language code exists.
        """
        return code in self.languages

    # ---------------------------------
    # Get Language Name
    # ---------------------------------

    def language_name(self, code):
        """
        Return language name from code.
        """
        return self.languages.get(
            code,
            "Unknown"
        )

    # ---------------------------------
    # Detect Language
    # ---------------------------------

    def detect_language(self, text):
        """
        Simple language detection.
        Replace with AI model later.
        """

        text = text.lower()

        if "namaste" in text:
            return "hi"

        elif "namaskara" in text:
            return "kn"

        elif "vanakkam" in text:
            return "ta"

        elif "namaskaram" in text:
            return "te"

        elif "hola" in text:
            return "es"

        elif "bonjour" in text:
            return "fr"

        elif "hallo" in text:
            return "de"

        return "en"

    # ---------------------------------
    # Total Languages
    # ---------------------------------

    def total_languages(self):
        """
        Return number of supported languages.
        """
        return len(self.languages)

    # ---------------------------------
    # Translation Count
    # ---------------------------------

    def translation_count(self):
        """
        Return total translations performed.
        """
        return len(self.history)

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):
        """
        Return module health.
        """

        return {

            "status": "Healthy",

            "supported_languages":
                self.total_languages(),

            "translations":
                self.translation_count()

        }

    # ---------------------------------
    # Reset History
    # ---------------------------------

    def reset_history(self):
        """
        Clear translation history.
        """

        self.history.clear()

        logging.info(
            "Translation history cleared."
        )

    # ---------------------------------
    # Module Summary
    # ---------------------------------

    def summary(self):
        """
        Return module summary.
        """

        return {

            "health":
                self.health(),

            "languages":
                self.supported_languages()

        }
    # ---------------------------------
    # Translate Text
    # ---------------------------------

    def translate(
        self,
        text,
        target_language="en"
    ):
        """
        Simulated translation.
        Replace this with Google Translate,
        Azure Translator or OpenAI later.
        """

        if not self.language_exists(
            target_language
        ):

            return {
                "success": False,
                "message": "Unsupported language."
            }

        source = self.detect_language(text)

        translated = f"[{self.languages[target_language]}] {text}"

        record = {

            "time": self.current_time(),

            "source": source,

            "target": target_language,

            "original": text,

            "translated": translated

        }

        self.history.append(record)

        return {

            "success": True,

            "source_language":
                self.languages[source],

            "target_language":
                self.languages[target_language],

            "translated_text":
                translated

        }

    # ---------------------------------
    # Chat Translation
    # ---------------------------------

    def translate_chat(
        self,
        message,
        language
    ):

        return self.translate(
            message,
            language
        )

    # ---------------------------------
    # Stadium Announcement
    # ---------------------------------

    def translate_announcement(
        self,
        announcement,
        language
    ):

        result = self.translate(
            announcement,
            language
        )

        result["type"] = "Announcement"

        return result

    # ---------------------------------
    # Emergency Alert Translation
    # ---------------------------------

    def translate_emergency(
        self,
        message,
        language
    ):

        result = self.translate(
            message,
            language
        )

        result["type"] = "Emergency"

        result["priority"] = "High"

        return result

    # ---------------------------------
    # Batch Translation
    # ---------------------------------

    def batch_translate(
        self,
        messages,
        language
    ):

        translated = []

        for message in messages:

            translated.append(

                self.translate(
                    message,
                    language
                )

            )

        return translated

    # ---------------------------------
    # Translation History
    # ---------------------------------

    def translation_history(self):

        return self.history
    # ---------------------------------
    # Most Used Language
    # ---------------------------------

    def most_used_language(self):

        if not self.history:
            return None

        usage = {}

        for item in self.history:

            language = item["target"]

            usage[language] = (
                usage.get(language, 0) + 1
            )

        code = max(
            usage,
            key=usage.get
        )

        return {

            "code": code,

            "language":
                self.language_name(code),

            "count":
                usage[code]

        }

    # ---------------------------------
    # Translation Statistics
    # ---------------------------------

    def statistics(self):

        return {

            "supported_languages":
                self.total_languages(),

            "translations":
                self.translation_count(),

            "most_used_language":
                self.most_used_language()

        }

    # ---------------------------------
    # Export History
    # ---------------------------------

    def export_history(self):

        return self.history

    # ---------------------------------
    # Export Report
    # ---------------------------------

    def export(self):

        return {

            "generated_at":
                self.current_time().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "statistics":
                self.statistics(),

            "history":
                self.export_history()

        }

    # ---------------------------------
    # AI Insights
    # ---------------------------------

    def insights(self):

        insights = []

        if self.translation_count() == 0:

            insights.append(
                "No translations available."
            )

            return insights

        most_used = self.most_used_language()

        insights.append(

            f"Most translated language: "
            f"{most_used['language']}"

        )

        insights.append(

            f"Total translations: "
            f"{self.translation_count()}"

        )

        return insights

    # ---------------------------------
    # Complete Summary
    # ---------------------------------

    def complete_summary(self):

        return {

            "health":
                self.health(),

            "statistics":
                self.statistics(),

            "insights":
                self.insights()

        }

    # ---------------------------------
    # Reset Module
    # ---------------------------------

    def reset(self):

        self.reset_history()

        logging.info(
            "Translation AI reset successfully."
        )

        return {

            "success": True,

            "message":
                "Translation history cleared."

        }