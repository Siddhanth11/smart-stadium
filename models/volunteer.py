from database import db
from datetime import datetime


class Volunteer(db.Model):
    __tablename__ = "volunteers"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    volunteer_id = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

    shift = db.Column(
        db.Enum("Morning", "Afternoon", "Evening", "Night"),
        nullable=False
    )

    assigned_gate = db.Column(db.String(20))

    assigned_zone = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    status = db.Column(
        db.Enum("Available", "Busy", "Off Duty"),
        default="Available"
    )

    experience = db.Column(db.Integer, default=0)

    joined_on = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref=db.backref("volunteer_profile", uselist=False)
    )

    def __repr__(self):
        return f"<Volunteer {self.volunteer_id}>"