from database import db
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)

    ticket_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    match_id = db.Column(
        db.Integer,
        db.ForeignKey("matches.id"),
        nullable=False
    )

    seat_number = db.Column(db.String(20))

    section = db.Column(db.String(50))

    gate = db.Column(db.String(20))

    qr_code = db.Column(db.String(255))

    price = db.Column(db.Float)

    payment_status = db.Column(
        db.Enum("Pending", "Paid", "Refunded"),
        default="Pending"
    )

    ticket_status = db.Column(
        db.Enum("Booked", "Checked-In", "Cancelled"),
        default="Booked"
    )

    booked_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Ticket {self.ticket_number}>"