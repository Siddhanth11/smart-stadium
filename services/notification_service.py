# services/notification_service.py

from datetime import datetime


class NotificationService:
    """
    Smart Stadium Notification Service
    """

    def __init__(self):

        self.notifications = []

    # ---------------------------------
    # Current Time
    # ---------------------------------

    def current_time(self):

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ---------------------------------
    # Send Notification
    # ---------------------------------

    def send(
        self,
        title,
        message
    ):

        notification = {

            "title": title,

            "message": message,

            "time": self.current_time()

        }

        self.notifications.append(notification)

        return {

            "success": True,

            "message": "Notification sent successfully."

        }

    # ---------------------------------
    # Ticket Confirmation
    # ---------------------------------

    def ticket_confirmation(
        self,
        user,
        match
    ):

        return self.send(

            "Ticket Confirmation",

            f"{user}, your ticket for {match} has been confirmed."

        )

    # ---------------------------------
    # Match Reminder
    # ---------------------------------

    def match_reminder(
        self,
        user,
        match
    ):

        return self.send(

            "Match Reminder",

            f"Hello {user}, your match '{match}' starts soon."

        )

    # ---------------------------------
    # Emergency Alert
    # ---------------------------------

    def emergency_alert(
        self,
        location
    ):

        return self.send(

            "Emergency Alert",

            f"Emergency reported near {location}. Please follow safety instructions."

        )

    # ---------------------------------
    # Crowd Alert
    # ---------------------------------

    def crowd_alert(
        self,
        zone
    ):

        return self.send(

            "Crowd Alert",

            f"Heavy crowd detected in {zone}. Please use an alternate route."

        )

    # ---------------------------------
    # Parking Alert
    # ---------------------------------

    def parking_alert(
        self,
        parking_zone
    ):

        return self.send(

            "Parking Alert",

            f"{parking_zone} is almost full. Please use another parking area."

        )

    # ---------------------------------
    # Get Notifications
    # ---------------------------------

    def get_notifications(self):

        return self.notifications

    # ---------------------------------
    # Clear Notifications
    # ---------------------------------

    def clear_notifications(self):

        self.notifications.clear()

        return {

            "success": True,

            "message": "All notifications cleared."

        }

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "service": "Notification Service",

            "status": "Running",

            "notifications": len(self.notifications)

        }


# Singleton Object

notification_service = NotificationService()