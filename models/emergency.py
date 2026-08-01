from database import db
from datetime import datetime


class Emergency(db.Model):
    __tablename__ = "emergencies"

    id = db.Column(db.Integer, primary_key=True)

    incident_type = db.Column(
        db.Enum(
            "Medical",
            "Fire",
            "Security",
            "Crowd",
            "Weather",
            "Other"
        ),
        nullable=False
    )

    severity = db.Column(
        db.Enum(
            "Low",
            "Medium",
            "High",
            "Critical"
        ),
        nullable=False
    )

    stadium_id = db.Column(
        db.Integer,
        db.ForeignKey("stadiums.id"),
        nullable=False
    )

    volunteer_id = db.Column(
        db.Integer,
        db.ForeignKey("volunteers.id")
    )

    location = db.Column(db.String(150))

    description = db.Column(db.Text)

    status = db.Column(
        db.Enum(
            "Reported",
            "In Progress",
            "Resolved"
        ),
        default="Reported"
    )

    reported_by = db.Column(db.String(100))

    reported_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    resolved_time = db.Column(db.DateTime)

    stadium = db.relationship(
        "Stadium",
        backref="emergencies"
    )

    volunteer = db.relationship(
        "Volunteer",
        backref="assigned_emergencies"
    )

    def __repr__(self):
        return f"<Emergency {self.id}>"