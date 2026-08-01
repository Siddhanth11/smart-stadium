# services/email_service.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailService:
    """
    Smart Stadium Email Service
    """

    def __init__(self):

        # Change these values with your email
        self.sender_email = "your_email@gmail.com"
        self.password = "your_app_password"

        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    # ---------------------------------
    # Send Email
    # ---------------------------------

    def send_email(
        self,
        receiver,
        subject,
        message
    ):

        try:

            email = MIMEMultipart()

            email["From"] = self.sender_email
            email["To"] = receiver
            email["Subject"] = subject

            email.attach(
                MIMEText(message, "plain")
            )

            server = smtplib.SMTP(
                self.smtp_server,
                self.smtp_port
            )

            server.starttls()

            server.login(
                self.sender_email,
                self.password
            )

            server.sendmail(
                self.sender_email,
                receiver,
                email.as_string()
            )

            server.quit()

            return {
                "success": True,
                "message": "Email sent successfully."
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # ---------------------------------
    # Ticket Confirmation Email
    # ---------------------------------

    def ticket_confirmation(
        self,
        receiver,
        match,
        seat
    ):

        subject = "Smart Stadium - Ticket Confirmation"

        message = f"""
Hello,

Your ticket has been confirmed.

Match : {match}
Seat  : {seat}

Thank you for choosing Smart Stadium.
"""

        return self.send_email(
            receiver,
            subject,
            message
        )

    # ---------------------------------
    # Match Reminder
    # ---------------------------------

    def match_reminder(
        self,
        receiver,
        match
    ):

        subject = "Match Reminder"

        message = f"""
Hello,

This is a reminder that your match

{match}

starts soon.

Please arrive at the stadium on time.
"""

        return self.send_email(
            receiver,
            subject,
            message
        )

    # ---------------------------------
    # Password Reset
    # ---------------------------------

    def password_reset(
        self,
        receiver,
        otp
    ):

        subject = "Password Reset"

        message = f"""
Your OTP is:

{otp}

Do not share this OTP with anyone.
"""

        return self.send_email(
            receiver,
            subject,
            message
        )

    # ---------------------------------
    # Emergency Notification
    # ---------------------------------

    def emergency_alert(
        self,
        receiver,
        alert
    ):

        subject = "Emergency Alert"

        message = f"""
Emergency Notification

{alert}

Please follow the instructions provided by stadium staff.
"""

        return self.send_email(
            receiver,
            subject,
            message
        )

    # ---------------------------------
    # Health Check
    # ---------------------------------

    def health(self):

        return {

            "service": "Email Service",

            "smtp_server": self.smtp_server,

            "status": "Ready"

        }


# Singleton Object

email_service = EmailService()